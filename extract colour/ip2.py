"""
Created on Fri Mar 26 16:25:50 2021

@author: python_seeker
"""

#how to do object tracking.
#By converting BGR to HSV

import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    #take each frame
    _,frame = cap.read()
    #convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #define range of colour u want, lets take for blue
    lower_range = np.array([40,40,40])
    upper_range = np.array([70,255,255])
    #threshold the HSV image to get only the colour
    mask=cv2.inRange(hsv,lower_range,upper_range)
    #Bitwise-AND mask and original image
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
cv2.destroyAllWindow()
# similarly for green color u can change the ranges