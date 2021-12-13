# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:48:54 2021

@author: karishni
"""

#import the Libraries
import cv2

img = cv2.imread('image.jpeg')

#create edge mask
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray_blur=cv2.medianBlur (gray,5)

#detect edge and enhance them
edges=cv2.adaptiveThreshold (gray_blur, 255, 
                             cv2.ADAPTIVE_THRESH_MEAN_C, cv2. THRESH_BINARY,9,9)

#colour quantization
color=cv2.bilateralFilter (img, 8, 250, 250)
#cartoonization
cartoon=cv2.bitwise_and (color, color, mask=edges)

cv2.imshow('image',img)
cv2.imshow('cartoon', cartoon)

cv2.waitKey(0)
cv2.destroyWindows ()
    