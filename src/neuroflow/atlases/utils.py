from pathlib import Path
from typing import Union

from nilearn import plotting


def qc_atlas_registration(atlas: Union[str, Path], reference: Union[str, Path], atlas_name: str, reference_name: str, force: bool = False):
    """
    Check if the registration of an atlas to a reference image was successful.

    Parameters
    ----------
    atlas : Union[str,Path]
        Path to the atlas image.
    reference : Union[str,Path]
        Path to the reference image.
    atlas_name : str
        Name of the atlas.
    reference_name : str
        Name of the reference image.
    force : bool, optional
        Force the registration, by default False
    """
    atlas = Path(atlas)
    reference = Path(reference)
    out_file = atlas.parent / atlas.name.replace("dseg.nii.gz", "QC.png")
    if out_file.exists() and not force:
        print(f"QC image {out_file} already exists.")
        return
    if not atlas.is_file():
        raise FileNotFoundError(f"Atlas {atlas} not found.")
    if not reference.is_file():
        raise FileNotFoundError(f"Reference {reference} not found.")

    _ = plotting.plot_roi(
        roi_img=atlas,
        bg_img=reference,
        title=f"{atlas_name} registration to {reference_name}",
        draw_cross=False,
        display_mode="ortho",
        annotate=False,
        alpha=0.5,
        output_file=out_file,
    )
