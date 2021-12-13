# -*- coding: utf-8 -*-
"""
Created on Sun Apr  12 12:42:10 2021

@author: karishni
"""

#how to do image segmentation!

import numpy as np
import cv2
from matplotlib import pyplot as plt

#load image
img = cv2.imread('coins.jpg')
#dislay loaded image
plt.subplot(241),plt.imshow(img),plt.title('Original')
# convert image to grey scale and threshold the image(divide foreground and background)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
plt.subplot(242),plt.imshow(thresh),plt.title('threshold')
# noise removal
kernel = np.ones((10,10),np.float32)/25
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
plt.subplot(243),plt.imshow(opening),plt.title('Opening')
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
plt.subplot(244),plt.imshow(sure_bg),plt.title('sure_bg')

#sure foreground
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
plt.subplot(245),plt.imshow(dist_transform),plt.title('dist_transform')
plt.subplot(246),plt.imshow(sure_fg),plt.title('sure_fg')
#unknown region
sure_fg=np.uint8(sure_fg)
unknown=cv2.subtract(sure_bg,sure_fg)
plt.subplot(247),plt.imshow(unknown),plt.title('unknown')
#marking label
ret, markers=cv2.connectedComponents(sure_fg)
markers=markers+1
#mark the region of unknown with 0
markers[unknown==255]=0
markers=cv2.watershed(img,markers)
img[markers==-1]=[255,0,0]
plt.subplot(248),plt.imshow(img),plt.title('result')

#click run















