"""
Participant Demographics Covariate Class
"""

from pathlib import Path
from typing import ClassVar
from typing import Union

import pandas as pd

from neuroflow.covariates.covariate import Covariate
from neuroflow.covariates.participant_demographics.utils import CRF_COLUMNS_TO_KEEP
from neuroflow.covariates.participant_demographics.utils import CRF_TRANSFORMATIONS
from neuroflow.covariates.participant_demographics.utils import get_worksheet
from neuroflow.covariates.participant_demographics.utils import load_or_request_credentials
from neuroflow.files_mapper.files_mapper import FilesMapper


class ParticipantDemographics(Covariate):
    """
    Class to handle the participant demographics data

    Attributes
    ----------
    mapper : FilesMapper
        The mapper to the files

    Methods
    -------
    _get_timestamp_from_session(session_id:str) -> datetime
        Parse the timestamp of a session from the session id
    """

    SUBJECT_ID_COLUMN: ClassVar = "Questionnaire"
    CRF_COLUMNS_TO_KEEP: ClassVar = CRF_COLUMNS_TO_KEEP
    CRF_TRANSFORMATIONS: ClassVar = CRF_TRANSFORMATIONS

    COVARIATE_SOURCE: ClassVar = "demographics"

    _crf = None

    def __init__(self, mapper: FilesMapper, google_credentials_path: Union[str, Path]):
        """
        Constructor for the ParticipantDemographics class

        Parameters
        ----------
        mapper : FilesMapper
            The mapper to the files
        """
        super().__init__(mapper)
        self.google_credentials_path = google_credentials_path

    def _load_crf(self, google_credentials_path: Union[str, Path]):
        """
        Load the CRF data from a Google Sheet

        Parameters
        ----------
        google_credentials_path : Union[str, Path]
            The path to the Google credentials
        """
        credentials = load_or_request_credentials(google_credentials_path)
        return get_worksheet(credentials)

    def locate_subject_row(self):
        """
        Locate the row of the subject in the CRF data
        """
        fixed_crf_subjects = self.crf[self.SUBJECT_ID_COLUMN].str.lower().str.zfill(4).str.replace("_", "")
        mask = fixed_crf_subjects == self.mapper.subject.lower()
        return self.crf.loc[mask]

    def get_subject_data(self):
        """
        Get the data of the subject from the CRF data
        """
        subject_row = self.locate_subject_row()
        subject_row = subject_row[list(self.CRF_COLUMNS_TO_KEEP.keys())].rename(columns=self.CRF_COLUMNS_TO_KEEP)
        for column, transformation in self.CRF_TRANSFORMATIONS.items():
            subject_row[column] = subject_row[column].apply(transformation)
        subject_row["age_at_scan"] = self._calculate_age_from_dob(subject_row)
        subject_row = subject_row.reset_index().rename({"index": "crf_index"})
        # add source identifier
        subject_row.loc["source"] = [self.COVARIATE_SOURCE] * len(subject_row.columns)
        return subject_row

    def _calculate_age_from_dob(self, subject_row: pd.DataFrame):
        """
        Calculate the age from the date of birth

        Parameters
        ----------
        dob : str
            The date of birth

        Returns
        -------
        int
            The age
        """
        dob = subject_row["dob"].iloc[0]
        return (self.session_timestamp - dob).days // 365

    @property
    def crf(self):
        """
        The CRF data
        """
        if self._crf is None:
            self._crf = self._load_crf(self.google_credentials_path)
        return self._crf
