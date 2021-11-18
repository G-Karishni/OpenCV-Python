# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 08:29:47 2021

@author: karish
"""

#retrieveing noised image

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noise.jpg')

kernel = np.ones((10,10),np.float32)/25


median = cv2.medianBlur(img,7)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median')
plt.xticks([]), plt.yticks([])

plt.show()





