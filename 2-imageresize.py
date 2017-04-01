# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 00:46:21 2017

@author: k
"""
import cv2
 

image = cv2.imread("jurassic.png")
cv2.imshow("original", image)
# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image
r = 300.0 / image.shape[1]
dim = (300, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)