"""
This file contains the available atlases that can be used in the pipeline.
"""

# ruff: noqa: E501


def generate_schaefer_dict() -> dict:
    """
    Generate a dictionary with the Schaefer 2018 atlases.

    Returns
    -------
    dict
        Dictionary with the Schaefer 2018 atlases.
    """
    schaefer_dict = {}
    for n_regions in range(100, 1001, 100):
        for n_networks in [7, 17]:
            schaefer_dict[f"schaefer2018_{n_regions}_{n_networks}"] = {
                "nifti": f"src/neuroflow/atlases/available_atlases/schaefer2018/MNI152/space-MNI152_atlas-schaefer2018_res-1mm_den-{n_regions}_desc-{n_networks}networks_dseg.nii.gz",
                "description": f"src/neuroflow/atlases/available_atlases/schaefer2018/MNI152/space-MNI152_atlas-schaefer2018_res-1mm_den-{n_regions}_desc-{n_networks}networks_dseg.csv",
                "label_name": "index",
            }
    return schaefer_dict


AVAILABLE_ATLASES = {
    "fan2016": {
        "nifti": "src/neuroflow/atlases/available_atlases/fan2016/MNI152/space-MNI152_atlas-fan2016_res-1mm_dseg.nii.gz",
        "description": "src/neuroflow/atlases/available_atlases/fan2016/MNI152/space-MNI152_atlas-fan2016_res-1mm_dseg.csv",
        "label_name": "Label",
    },
    "huang2022": {
        "nifti": "src/neuroflow/atlases/available_atlases/huang2022/MNI152/space-MNI152_atlas-huang2022_res-1mm_dseg.nii.gz",
        "description": "src/neuroflow/atlases/available_atlases/huang2022/MNI152/space-MNI152_atlas-huang2022_res-1mm_dseg.csv",
        "label_name": "HCPex_label",
    },
    **generate_schaefer_dict(),
}
