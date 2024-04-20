"""
ConnectomeReconstructor class for NeuroFlow.
"""

from pathlib import Path
from typing import ClassVar, Optional

from neuroflow.atlases.atlases import Atlases
from neuroflow.connectome.utils import COMBINATIONS
from neuroflow.files_mapper import FilesMapper


class ConnectomeReconstructor:
    """
    ConnectomeReconstructor class for NeuroFlow.
    A class to reconstruct connectomes from tractography data.
    """

    OUTPUT_TEMPLATE: ClassVar = (
        "{atlas}/sub-{subject}_ses-{session}_space-dwi_atlas-{atlas}_scale-{scale}_meas-{stat_edge}_{suffix}.csv"  # noqa: E501
    )
    RECONSTRUCTION_COMBINATIONS: ClassVar = COMBINATIONS.copy()

    DIRECTORY_NAME: ClassVar = "connectomes"

    def __init__(
        self,
        mapper: FilesMapper,
        atlases_manager: Atlases,
        output_directory: Optional[str] = None,
    ):
        """
        Initialize the ConnectomeReconstructor class.

        Parameters
        ----------
        mapper : FilesMapper
            An instance of FilesMapper class.
        atlases_manager : Atlases
            An instance of Atlases class.
        output_directory : str
            Path to the output directory.
        """
        self.mapper = mapper
        self.atlases_manager = atlases_manager
        self.output_directory = self._gen_output_directory(output_directory)

    def _gen_output_directory(self, output_directory: Optional[str] = None) -> Path:
        """
        Generate output directory for QC measures.

        Parameters
        ----------
        output_directory : Optional[str], optional
            Path to the output directory, by default None

        Returns
        -------
        Path
            Path to the output directory
        """
        if output_directory is None:
            return None
        output_directory = Path(output_directory)
        flags = [
            output_directory.parent.name == f"ses-{self.mapper.session}",
            output_directory.parent.parent.name == f"sub-{self.mapper.subject}",
        ]
        if all(flags):
            output_directory = output_directory / self.DIRECTORY_NAME
        else:
            output_directory = (
                Path(output_directory)
                / f"sub-{self.mapper.subject}"
                / f"ses-{self.mapper.session}"
                / self.DIRECTORY_NAME
            )
        output_directory.mkdir(parents=True, exist_ok=True)
        return output_directory
