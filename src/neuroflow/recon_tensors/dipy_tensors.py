from pathlib import Path
from typing import Union

from neuroflow.files_mapper.files_mapper import FilesMapper
from neuroflow.recon_tensors.recon_tensors import ReconTensors


class DipyTensors(ReconTensors):
    """
    Reconstruction of diffusion tensors from the diffusion signal using Dipy.
    """

    def __init__(
        self,
        mapper: FilesMapper,
        out_dir: Union[str, Path],
        max_bvalue: int = None,  # noqa
        bval_tol: int = 50,
    ):
        """
        Initialize the DipyTensors class.

        Parameters
        ----------
        mapper : FilesMapper
            An instance of FilesMapper class.
        out_dir : Union[str, Path]
            Path to the output directory.
        max_bvalue : int
            Maximum b-value to use for the reconstruction.
        """
        super().__init__(mapper, out_dir, max_bvalue, bval_tol)
