# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:48:54 2021

@author: karishni
"""

import cv2 as cv

#define and create videowriter object
fourcc = cv.VideoWriter_fourcc(*"XVID")
out=cv.VideoWriter('output.avi', fourcc, 20, (480,480))

while cap.isOpened():
       ret, frame = cap.read()
       inverted = cv.flip (frame, 0)
       #flip fn is used to flip the video frame
       out.write(inverted)
       cv.imshow("frame", frame)
       cv.imshow("inverted frame", inverted)
       if cv.waitkey(1) ==ord('q'):
             break

cap.release()
out.release()
cv.destroyAllWindows()

#NOW Click Run!!