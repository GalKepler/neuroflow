from pathlib import Path
from typing import ClassVar
from typing import Optional

from neuroflow.covariates import Covariate
from neuroflow.files_mapper.files_mapper import FilesMapper


class QCManager(Covariate):
    """
    QCManager class is responsible for gathering all QC
    measures available for a participant.
    """

    DIRECTORY_NAME: ClassVar[str] = "quality_control"

    def __init__(self, files_mapper: FilesMapper, output_directory: Optional[str] = None):
        super().__init__(output_directory)
        self.files_mapper = files_mapper
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
        output_directory = (
            Path(output_directory) / f"sub-{self.files_mapper.subject}" / f"ses-{self.files_mapper.session}" / self.DIRECTORY_NAME
        )
        output_directory.mkdir(parents=True, exist_ok=True)
        return output_directory

    def _collect_qc_measures(self):
        """
        Collect QC measures for the participant.
        """
