"""
Reconstruction of diffusion tensors from the diffusion signal.
"""

from pathlib import Path
from typing import ClassVar
from typing import Optional
from typing import Union

from nipype.interfaces.mrtrix3 import DWIExtract

from neuroflow.files_mapper.files_mapper import FilesMapper


class ReconTensors:
    """
    Reconstruction of diffusion tensors from the diffusion signal.
    """

    OUTPUTS: ClassVar = []
    OUTPUT_TEMPLATE: ClassVar = (
        "{software}/sub-{subject}_ses-{session}_space-dwi_acq-shell{max_bvalue}_rec-{software}_desc-{metric}_dwiref.nii.gz"
    )

    def __init__(self, mapper: FilesMapper, out_dir: Union[str, Path], max_bvalue: Optional[int] = 1000, bval_tol: Optional[int] = 50):
        """
        Initialize the ReconTensors class.

        Parameters
        ----------
        mapper : FilesMapper
            An instance of FilesMapper class.
        out_dir : Union[str, Path]
            Path to the output directory.
        max_bvalue : int
            Maximum b-value to use for the reconstruction.
        """
        self.mapper = mapper
        self.out_dir = Path(out_dir)
        self.filtered_bvalues = self._filter_bvalues(max_bvalue, bval_tol)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.software = None

    def _filter_bvalues(self, max_bvalue: Optional[int] = 1000, bval_tol: Optional[int] = 50) -> int:
        """
        Filter the b-values based on the maximum b-value.
        """
        bvals = self._read_bvals()
        if max_bvalue is None:
            filtered_bvals = list(set(bvals))
        else:
            filtered_bvals = [bval for bval in bvals if bval <= max_bvalue + bval_tol]
        return list(set([round(bval, -2) for bval in filtered_bvals]))  # noqa

    def _read_bvals(self) -> list[int]:
        """
        Read the b-values from the bvals file.
        """
        bvals_file = self.mapper.files.get("bval_file")
        with Path.open(bvals_file, encoding="utf-8") as f:
            bvals = [int(val) for val in f.readline().split()]
        return bvals

    def crop_to_max_bvalue(self):
        """
        Crop the diffusion signal to the maximum b-value.
        """
        out_template = str(self.out_dir / f"sub-{self.mapper.subject}_ses-{self.mapper.session}_acq-shell{self.max_bvalue}_dwi")
        out_files = {}
        for key, extension in zip(["dwi_file", "bval_file", "bvec_file"], [".nii.gz", ".bval", ".bvec"]):
            out_files[key] = Path(out_template + extension)
        if all([out_file.exists() for out_file in out_files.values()]):  # noqa
            return out_files
        dwiextract = DWIExtract()
        dwiextract.inputs.in_file = self.mapper.files.get("dwi_file")
        dwiextract.inputs.grad_fsl = (self.mapper.files.get("bvec_file"), self.mapper.files.get("bval_file"))
        dwiextract.inputs.out_file = out_files.get("dwi_file")
        dwiextract.inputs.out_bvec = out_files.get("bvec_file")
        dwiextract.inputs.out_bval = out_files.get("bval_file")
        dwiextract.inputs.shell = self.filtered_bvalues
        dwiextract.run()
        return out_files

    def collect_outputs(self) -> dict:
        """
        Gather outputs for the DipyTensors workflow.

        Returns
        -------
        dict
            Outputs for the DipyTensors workflow.
        """
        return {
            key: self.out_dir
            / self.OUTPUT_TEMPLATE.format(
                subject=self.mapper.subject,
                session=self.mapper.session,
                max_bvalue=self.max_bvalue,
                software=self.software,
                metric=key,
            )
            for key in self.OUTPUTS
        }

    def run(self, force: bool = False) -> dict:
        """
        Run the workflow.

        Returns
        -------
        dict
            Outputs for the workflow.
        """
        raise NotImplementedError

    @property
    def filtered_files(self) -> dict:
        """
        Get the filtered files.
        """
        return self.crop_to_max_bvalue()

    @property
    def max_bvalue(self) -> int:
        """
        Get the maximum b-value (rounded to the nearest 100)
        """
        return round(max(self.filtered_bvalues), -2)

    @property
    def outputs(self) -> dict:
        """
        Get the outputs.
        """
        return self.run()
