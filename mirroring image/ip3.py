# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:27:38 2021

@author: karish
"""
#how to find the mirror image of loaded image

import cv2
import numpy as np
 
# Read the image
img = cv2.imread('youtube.png')
rows, cols = img.shape[:2]
# Define the 3 pairs of corresponding points 
input_pts = np.float32([[0,0], [cols-1,0], [0,rows-1]])
output_pts = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])
# Calculate the transformation matrix using cv2.getAffineTransform()
M= cv2.getAffineTransform(input_pts , output_pts)
# Apply the affine transformation using cv2.warpAffine()
dst = cv2.warpAffine(img, M, (cols,rows))
# Display the image
out = cv2.hconcat([img, dst])

#for displaying only the mirror img
cv2.imshow('Output', dst)
cv2.waitKey(0)

#click run.
#THANK YOU FOR WATCHING!!!