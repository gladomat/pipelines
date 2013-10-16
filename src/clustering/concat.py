import numpy as np
import nibabel as nb
import os
from similarity import Similarity
import nipype.interfaces.afni as afni

from utils import get_mask

preprocessedfile = '/scr/ilz1/Data/results/preprocessed_resting/_session_session1/_subject_id_9630905/_fwhm_0/_bandpass_filter0/afni_corr_rest_roi_dtype_tshift_detrended_regfilt_gms_filt.nii.gz'
sxfm = nb.load('/scr/schweiz1/Data/results/sxfmout/_session_session1/_subject_id_9630905/_fwhm_0/_hemi_lh/lh.afni_corr_rest_roi_dtype_tshift_detrended_regfilt_gms_filt.fsaverage4.nii').get_data()
maskedinput = nb.load('/scr/kongo1/NKIMASKS/masks/inputfile.nii').get_data()


##CONCATENATE INPUT##
volumeinput = maskedinput[np.where(targetmask)]
surfaceinput = np.squeeze(sxfm)
totalinput = np.concatenate((surfaceinput,volumeinput))

##CONCATENATE TARGET##

#run Similarity
corr = afni.AutoTcorrelate()  #3dWarp -deoblique ??
corr.inputs.in_file = concatenatedfile
corr.inputs.mask = targetxfm_result.outputs.out_file
corr.inputs.mask_only_targets = True
corr.inputs.out_file = os.path.join(workingdir,'masks/','corr_out.1D')
corr_result = corr.run()

#convert from AFNI file to NIFTI
convert = afni.AFNItoNIFTI()
convert.inputs.in_file = corr_result.outputs.out_file
convert.inputs.out_file = corr_result.outputs.out_file + '.nii'
convert_result = convert.run()
