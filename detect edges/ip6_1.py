# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:05:37 2021

@author: karish
"""
#detect edges using uploaded image

import cv2
import numpy as np

frame=cv2.imread(sudoku.png)
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150,apertureSize=3)

cv2.imshow('edges',edges)
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=500,maxLineGap=1)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
    
    cv2.imshow('image',frame)

cv2.destroyAllWindows()    

