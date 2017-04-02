# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 00:13:08 2017

@author: k
"""
import cv2
image = cv2.imread("jurassic.png")
# crop the image using array slices -- it's a NumPy array  after all!
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)