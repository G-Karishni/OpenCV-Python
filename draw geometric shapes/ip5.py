# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:48:19 2021

@author: karish
"""
#how to represent geometric shapes using python

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)             #create a black image
img = cv2.line(img,(0,0),(511,511),(0,255,0),5)   #draw a diagnol blue line with thickness 5px
cv2.imshow('output',img)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)    #(img,start point,end point,line colour(r,g,b),thickness)
cv2.imshow('output',img)
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)      #(img,origin,radius,line colour(r,g,b),thickness(-1 for full colour))
cv2.imshow('output',img)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)  #(img,origin,radius,line colour(r,g,b),thickness(-1 for full colour))   
cv2.imshow('output',img)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))           #(img,corner points of polygon,boolean,line color(r,g,b))
cv2.imshow('output',img)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'PYTHON SEEKERS',(20,500), font, 1.5,(255,255,255),2,cv2.LINE_AA)
#(img,text , location,font style,font colour(r,g,b),line type)
cv2.imshow('output',img)
#click run


