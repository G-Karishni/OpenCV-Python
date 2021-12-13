# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:48:54 2021

@author: karishni
"""

import cv2
import imutils

#initializing the HOG person detector

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#Load the video (place it in the same path as the source code) 
cap = cv2.VideoCapture('vid.mp4')
while cap.isopened():
     ret, image=cap.read()
     if ret:
        image= imutils.resize(image,width=min(400, image.shape[1])) 
        #detect all the regions that has pedestrians 
        (region,_) = hog.detectMultiscale(image,winStride=(4, 4),padding=(4, 4),scale=1.05) 
        #draw the regions in the video
        for (x,y,w,h) in region: 
            cv2.rectangle(image, (x, y),(x, y + h),(0, 0, 255), 2)

     cv2.imshow("Image", image)
     if cv2.waitkey(25) & 0xFF== ord('q'):
        break

cv2.destroyAllwindows()
#Done! Click Run.