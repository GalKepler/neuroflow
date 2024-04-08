"""
Registrations of atlases to subject's diffusion space.
"""

import copy
from pathlib import Path
from typing import ClassVar
from typing import Optional
from typing import Union

from nipype.interfaces import fsl

from neuroflow.atlases.available_atlases.available_atlases import AVAILABLE_ATLASES
from neuroflow.atlases.utils import qc_atlas_registration
from neuroflow.files_mapper.files_mapper import FilesMapper


class Atlases:
    """
    Registrations of atlases to subject's diffusion space.
    """

    ATLASES: ClassVar = AVAILABLE_ATLASES
    OUTPUT_TEMPLATE: ClassVar = "sub-{subject}_ses-{session}_space-{space}_{atlas}"

    def __init__(self, mapper: FilesMapper, out_dir: Union[str, Path], atlases: Optional[Union[str, list]] = None):
        """
        Initialize the Atlases class.

        Parameters
        ----------
        mapper : FilesMapper
            An instance of FilesMapper class.
        out_dir : Union[str, Path]
            Path to the output directory.
        """
        self.mapper = mapper
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(exist_ok=True, parents=True)
        self.atlases = self._validate_atlas(atlases)

    def _validate_atlas(self, atlases: Union[str, list]):
        """
        Validate that the provided atlas is included in the available atlases.
        """
        if atlases is None:
            return self.ATLASES
        if isinstance(atlases, str):
            atlases = [atlases]
        for atlas in atlases:
            if atlas not in self.ATLASES:
                raise ValueError(f"Atlas {atlas} is not available.")
        return {atlas: self.ATLASES[atlas] for atlas in atlases}

    def register_atlas_to_t1w(self, force: bool = False):
        """
        Register an atlas to the subject's T1w space.
        """
        t1w_atlases = copy.deepcopy(self.atlases)
        for atlas, atlas_entities in self.atlases.items():
            nifti = atlas_entities["nifti"]
            atlas_base = Path(nifti).name.replace("space-MNI152_", "")
            out_file = self.out_dir / self.OUTPUT_TEMPLATE.format(
                subject=self.mapper.subject,
                session=self.mapper.session,
                space="T1w",
                atlas=atlas_base,
            )
            t1w_atlases[atlas]["nifti"] = str(out_file)
            if force:
                out_file.unlink(missing_ok=True)
            if out_file.exists():
                continue
            aw = fsl.ApplyWarp(datatype="int", interp="nn", out_file=str(out_file))
            aw.inputs.in_file = nifti
            aw.inputs.ref_file = self.mapper.files.get("t1w_brain")
            aw.inputs.mask_file = self.mapper.files.get("t1w_brain_mask")
            aw.inputs.field_file = self.mapper.files.get("template_to_t1w_warp")
            aw.run()
            qc_atlas_registration(out_file, self.mapper.files.get("t1w_brain"), atlas, "T1w", force=force)
        return t1w_atlases

    def register_atlas_to_dwi(self, force: bool = False):
        """
        Register an atlas to the subject's diffusion space.
        """
        dwi_atlases = copy.deepcopy(self.atlases)
        for atlas, atlas_entities in self.atlases.items():
            nifti = atlas_entities["nifti"]
            in_file = self.t1w_atlases[atlas]["nifti"]
            atlas_base = Path(nifti).name.replace("space-MNI152_", "")
            out_file = self.out_dir / self.OUTPUT_TEMPLATE.format(
                subject=self.mapper.subject,
                session=self.mapper.session,
                space="dwi",
                atlas=atlas_base,
            )
            dwi_atlases[atlas]["nifti"] = str(out_file)
            if force:
                out_file.unlink(missing_ok=True)
            if out_file.exists():
                continue
            apply_xfm = fsl.ApplyXFM(datatype="int", interp="nearestneighbour", out_file=str(out_file))
            apply_xfm.inputs.in_file = in_file
            apply_xfm.inputs.reference = self.mapper.files.get("b0_brain")
            apply_xfm.inputs.in_matrix_file = self.mapper.files.get("t1w_to_dwi_mat")
            apply_xfm.run()
            qc_atlas_registration(out_file, self.mapper.files.get("b0_brain"), atlas, "DWI", force=force)
        return dwi_atlases

    @property
    def t1w_atlases(self):
        """
        Register the atlases to the T1w space.
        """
        return self.register_atlas_to_t1w()

    @property
    def dwi_atlases(self):
        """
        Register the atlases to the diffusion space.
        """
        return self.register_atlas_to_dwi()
