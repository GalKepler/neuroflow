from pathlib import Path
from typing import ClassVar
from typing import Union

from nipype.interfaces import fsl

from neuroflow.covariates.covariate import Covariate
from neuroflow.files_mapper.files_mapper import FilesMapper


class QualityControl(Covariate):
    """
    Class to handle the quality control covariates

    Attributes
    ----------
    mapper : FilesMapper
        The mapper to the files

    Methods
    -------
    get_covariates() -> dict
        Get the quality control covariates
    """

    COVARIATE_SOURCE: ClassVar = "QC"

    def __init__(self, mapper: FilesMapper, out_dir: Union[str, Path]):
        """
        Constructor for the QualityControl class

        Parameters
        ----------
        mapper : FilesMapper
            The mapper to the files
        """
        super().__init__(mapper)
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)

    def _fix_file_name(self, file: Path):
        """
        Fix the file name

        Parameters
        ----------
        file : Path
            The file to fix the name
        """
        new_file = file.with_name(file.name.replace("data.nii.gz.", "data."))
        return new_file

    def _pre_eddy_qc(self):
        """
        Prepare the eddy quality control
        """
        base_dir = self.mapper.files.get("bval_file").parent
        changed_files = {}
        for file in base_dir.glob("data.nii.gz.*"):
            # Rename the files
            new_file = self._fix_file_name(file)
            changed_files[str(file)] = str(new_file)
            file.rename(new_file)
        return changed_files

    def _post_eddy_qc(self, changed_files: dict):
        """
        Post process the eddy quality control
        """
        for old_file, new_file in changed_files.items():
            file = Path(new_file)
            file.rename(old_file)

    def _prepare_inputs(self):
        inputs = {
            "bval_file": self._fix_file_name(self.mapper.files.get("bval_file")),
            "bvec_file": self._fix_file_name(self.mapper.files.get("bvec_file")),
            "mask_file": self._fix_file_name(self.mapper.files.get("b0_brain_mask")),
            "idx_file": self._fix_file_name(self.mapper.files.get("index_file")),
            "param_file": self._fix_file_name(self.mapper.files.get("param_file")),
        }
        inputs["base_name"] = str(inputs["bval_file"].parent / "data")
        return inputs

    def _run_eddy_qc(self):
        """
        Run the eddy quality control
        """
        inputs = self._prepare_inputs()
        changed_files = self._pre_eddy_qc()
        eddy_qc = fsl.EddyQuad(**inputs)
        eddy_qc.inputs.output_dir = str(self.out_dir / "eddy_qc")
        res = eddy_qc.run()
        self._post_eddy_qc(changed_files)
        return res

    def get_covariates(self) -> dict:
        """
        Get the quality control covariates

        Returns
        -------
        dict
            The quality control covariates
        """
        return {"quality_control": self.mapper.get_quality_control()}
