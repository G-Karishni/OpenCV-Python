# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:30:53 2021

@author: python_seeker
"""
#how to load and display an image!!
#note: Make sure that the image file actually exists at the specified path
# the image and source code has to placed in the same folder.

import cv2

img=cv2.imread('youtube.png',0)  #load an color image in grey scale 
cv2.imshow('first image',img)    #displaying the loaded image
cv2.waitKey(0)                   #the image will be visible untill key is pressed
cv2.destroyAllWindows()

#click run.
#when any key is pressed the image is removed







