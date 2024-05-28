import os
import shutil
from pathlib import Path
from typing import ClassVar, Optional, Union

from neuroflow.files_mapper.files_mapper import FilesMapper
from neuroflow.structural.utils import build_smriprep_command


class SMRIPrepRunner:
    """
    Run the sMRIPrep pipeline on the input data.
    """

    DIRECTORY_NAME: ClassVar = "smriprep"
    BIDS_DIRECTORY: ClassVar = "bids"

    T1_DESTINATION: ClassVar = (
        "{bids_directory}/sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_T1w.nii.gz"
    )
    T1_key = "t1w"

    def __init__(
        self,
        mapper: FilesMapper,
        output_directory: Union[str, Path],
        fs_license_file: Optional[Path] = None,
    ):
        self.mapper = mapper
        self.output_directory = self._gen_output_directory(output_directory)
        self.bids_directory = self._gen_bids_directory()
        self.fs_license_file = self._get_fs_license_file(fs_license_file)

    def _get_fs_license_file(self, fs_license_file: Path) -> Path:
        """
        Get the FreeSurfer license file.

        Parameters
        ----------
        fs_license_file : Path
            Path to the FreeSurfer license file.

        Returns
        -------
        Path
            Path to the FreeSurfer license file.
        """
        if not fs_license_file:
            if os.getenv("FS_LICENSE"):
                return Path(os.getenv("FS_LICENSE"))
            else:
                fs_home = os.getenv("FREESURFER_HOME")
                fs_license_file = Path(fs_home) / "license.txt"
                if not fs_license_file.exists():
                    raise ValueError("FreeSurfer license file not found.")
        return Path(fs_license_file)

    def _gen_bids_directory(self) -> Path:
        """
        Generate the BIDS directory for the sMRIPrep pipeline.

        Returns
        -------
        Path
            Path to the BIDS directory.
        """
        bids_directory = Path(
            str(self.output_directory).replace(self.DIRECTORY_NAME, self.BIDS_DIRECTORY)
        )
        t1_destination = Path(
            self.T1_DESTINATION.format(
                bids_directory=bids_directory,
                subject=self.mapper.subject,
                session=self.mapper.session,
            )
        )
        if not t1_destination.exists():
            t1_destination.parent.mkdir(parents=True, exist_ok=True)
            # make a copy of the T1w image (not symlink)
            t1_source = self.mapper.files.get(self.T1_key)
            shutil.copy(t1_source, t1_destination)

        return bids_directory

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

    def run(self):
        """
        Run the sMRIPrep pipeline.
        """
        command = build_smriprep_command(
            bids_directory=self.bids_directory,
            output_directory=self.output_directory,
            fs_license_file=self.fs_license_file,
            subject_id=self.mapper.subject,
        )
        print("Running sMRIPrep pipeline...")
        print(" ".join(command))
        # subprocess.run(command)
        print("sMRIPrep pipeline finished.")
