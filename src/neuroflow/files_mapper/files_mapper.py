class FilesMapper:
    def __init__(self, path: str, patterns: dict):
        """
        Initialize the FilesMapper object.
        This object is used to map files to their respective patterns.

        Parameters
        ----------
        path : str
            Path to the directory containing the files to be mapped.
        patterns : dict
            Dictionary containing the patterns to be used to map the files.
            The keys are file types and the values are the corresponding patterns.
        """
        self.path = path
        self.patterns = patterns
        self.files = self._get_files()

    # def _get_files(self) -> dict:
