from typing import ClassVar

from neuroflow.covariates.covariate import Covariate
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

    TIMESTAMP_FORMAT: ClassVar = "%Y%m%d%H%M"

    COVARIATE_SOURCE: ClassVar = "temporal"

    _crf = None

    def __init__(self, mapper: FilesMapper):
        """
        Constructor for the ParticipantDemographics class

        Parameters
        ----------
        mapper : FilesMapper
            The mapper to the files
        """
        super().__init__(mapper)
