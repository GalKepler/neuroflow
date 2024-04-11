from neuroflow.files_mapper.files_mapper import FilesMapper
from datetime import datetime
class ParticipantDemographics:
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

    TIMESTAMP_FORMAT = '%Y%m%d%H%M'

    def __init__(self,mapper: FilesMapper):
        """
        Constructor for the ParticipantDemographics class

        Parameters
        ----------
        mapper : FilesMapper
            The mapper to the files
        """
        self.mapper = mapper
        self.session_timestamp = self._get_timestamp_from_session(self.mapper.session)

    def _get_timestamp_from_session(self,session_id:str) -> datetime:
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
            return datetime.strptime(session_id,self.TIMESTAMP_FORMAT)
        except ValueError:
            return None