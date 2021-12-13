# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:48:54 2021

@author: karishni
"""

#image transformations - erosion and dilation

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("image.jpeg",-1)
#Load the image keep it in some path

kernel = np.ones ((5,5), np.uint8)
erosion = cv.erode (img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)

#erode fn will erodes the boundaries of foreground objects 
#dilation fn will increase the boundaries of foreground objects

plt.subplot(311),plt.imshow(img),plt.title('image') 
plt.subplot(312),plt.imshow(erosion),plt.title('erosion') 
plt.subplot(313),plt.imshow(dilation),plt.title('dilation')

#CLICK RUN