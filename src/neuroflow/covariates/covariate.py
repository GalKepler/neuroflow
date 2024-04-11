from neuroflow.files_mapper.files_mapper import FilesMapper


class Covariate:
    """
    Class to handle the covariate data
    """

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
