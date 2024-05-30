SMRIPREP_OUTPUTS = {
    "smriprep": {
        # T1w-related outputs
        "preprocessed_T1w": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_desc-preproc_T1w.nii.gz",
        "brain_mask": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_desc-brain_mask.nii.gz",
        "MNI_preprocessed_T1w": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_space-MNI152NLin2009cAsym_desc-preproc_T1w.nii.gz",
        "MNI_brain_mask": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz",
        # Transformations
        "mni_to_native_transform": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_from-MNI152NLin2009cAsym_to-T1w_mode-image_xfm.h5",
        "native_to_mni_transform": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_from-T1w_to-MNI152NLin2009cAsym_mode-image_xfm.h5",
        "fsnative_to_native_transform": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_from-fsnative_to-T1w_mode-image_xfm.txt",
        "native_to_fsnative_transform": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_from-T1w_to-fsnative_mode-image_xfm.txt",
        # Segmentation outputs
        "segmentation": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_desc-aparcaseg_dseg.nii.gz",
        "brainmask": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_desc-brain_mask.nii.gz",
        "probseg_gm": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_label-GM_probseg.nii.gz",
        "probseg_wm": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_label-WM_probseg.nii.gz",
        "probseg_csf": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_label-CSF_probseg.nii.gz",
        "summary": "sub-{subject}/ses-{session}/anat/sub-{subject}_ses-{session}_desc-summary.html",
        # Add other necessary output paths as needed
    },
    "freesurfer": {
        "fsaverage": "freesurfer/fsaverage/mri/brain.mgz",
        "T1w": "freesurfer/sub-{subject}/mri/T1.mgz",
        "brainmask": "freesurfer/sub-{subject}/mri/brainmask.mgz",
        "brain": "freesurfer/sub-{subject}/mri/brain.mgz",
        "wm": "freesurfer/sub-{subject}/mri/wm.mgz",
        "lh_pial": "freesurfer/sub-{subject}/surf/lh.pial",
        "rh_pial": "freesurfer/sub-{subject}/surf/rh.pial",
    },
}
