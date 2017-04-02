# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 00:18:52 2017

@author: k
"""
import cv2
image = cv2.imread("jurassic.png")
# write the cropped image to disk in jpg format
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)
cv2.imwrite("thumbnail.jpg", cropped)
cv2.waitKey(0)