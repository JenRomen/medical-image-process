import scipy, numpy, shutil, os, nibabel
import sys, getopt
import imageio
import numpy as np  
import nibabel as nib   # read nii data


filepath = ''
# list the file
import os

all_files,all_dirs=[],[]

for root, dirs, files in os.walk(filepath):
    for file in files:
        all_files.append(os.path.join(root,file))
        
    for dir in dirs:
        all_dirs.append(os.path.join(root,dir))
        
# nii to png        
num = 1
outputfile = ''
for filename in all_files:
    if filename[29:53] == 'PROCESSED\\MPRAGE\\T88_111' and filename[-3:-1] == "im" and filename[-14:-1] != 'masked_gfc.im': # check: if or regular
        img = nib.load(filename)
        imgg = img.dataobj[:,:,:,0]
        for current_slice in range(30, 120):

            data = imgg[:,:,current_slice]

            print('Saving image...')
            image_name = filename[54:80] + str(num) + str(current_slice) + ".png"
            imageio.imwrite(image_name, data)
            print('Saved.')

            # move images to folder
            print('Moving image...')
            src = image_name
            shutil.move(src, outputfile)
            print('Moved.')
        num += 1