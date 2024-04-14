from datetime import datetime
from typing import ClassVar

from neuroflow.files_mapper.files_mapper import FilesMapper


class Covariate:
    """
    Class to handle the covariate data
    """

    TIMESTAMP_FORMAT: ClassVar = "%Y%m%d%H%M"
    COVARIATE_SOURCE = None

    def __init__(self, mapper: FilesMapper):
        """
        Constructor for the Covariate class

        Parameters
        ----------
        mapper : FilesMapper
            The mapper to the files
        """
        self.mapper = mapper
        self.session_timestamp = self._get_timestamp_from_session(self.mapper.session)

    def _get_timestamp_from_session(self, session_id: str) -> datetime:
        """
        Parse the timestamp of a session from the session id

        Parameters
        ----------
        session_id : str
            The id of the session

        Returns
        -------
        datetime
            The timestamp of the session
        """
        try:
            return datetime.strptime(session_id, self.TIMESTAMP_FORMAT)  # noqa: DTZ007
        except ValueError:
            return None
