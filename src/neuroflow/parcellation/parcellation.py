"""
Parcellation module for NeuroFlow.
"""

from pathlib import Path
from typing import Callable
from typing import ClassVar
from typing import Optional
from typing import Union

from neuroflow.atlases.atlases import Atlases
from neuroflow.parcellation.available_measures import AVAILABLE_MEASURES
from neuroflow.recon_tensors.recon_tensors import ReconTensors


class Parcellation:
    """
    Parcellation class for NeuroFlow.
    """

    OUTPUT_TEMPLATE: ClassVar = "sub-{subject}_ses-{session}_space-{space}_atlas-{atlas}_meas-{measure}_parc.nii.gz"
    MEASURES: ClassVar = AVAILABLE_MEASURES

    def __init__(
        self,
        tensors_manager: ReconTensors,
        atlases_manager: Atlases,
        out_dir: Union[str, Path],
        measures: Optional[Union[str, list]] = None,
    ):
        """
        Initialize the Parcellation class.

        Parameters
        ----------
        tensors_manager : ReconTensors
            An instance of ReconTensors class.
        atlases_manager : Atlases
            An instance of Atlases class.
        out_dir : Union[str, Path]
            Path to the output directory.
        """
        self.tensors_manager = tensors_manager
        self.atlases_manager = atlases_manager
        self.mapper = self.tensors_manager.mapper
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.measures = self._validate_measures(measures)

    def _validate_measures(self, measures: Union[str, list]) -> Callable:
        """
        Validate the measure.

        Parameters
        ----------
        measure : str
            Measure to validate.

        Returns
        -------
        Callable
            Measure function.
        """
        if measures is None:
            return self.MEASURES
        if isinstance(measures, str):
            measures = [measures]
        for measure in measures:
            if measure not in self.MEASURES:
                raise ValueError(f"Invalid measure: {measure}.")
        return {measure: self.MEASURES[measure] for measure in measures}
