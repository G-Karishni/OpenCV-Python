# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:48:54 2021

@author: karishni
"""

import numpy as np
import cv2

img = cv2.imread('OIP.jpg')
cv2.imshow('frame',img)
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img1 = img*mask2[:,:,np.newaxis]
cv2.imshow('foreground',img1)
    