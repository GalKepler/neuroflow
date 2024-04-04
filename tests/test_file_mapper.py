"""
Test the file_mapper module.
"""

import pytest

from neuroflow.files_mapper.files_mapper import FilesMapper


def test_files_mapper():
    """
    Test the FilesMapper class.
    """
    mapper = FilesMapper("data/0001/1")
    # check that calling "files" raises an error
    with pytest.raises(FileNotFoundError):
        files = mapper.files  # noqa
