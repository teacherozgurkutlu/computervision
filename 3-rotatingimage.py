# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 00:03:10 2017

@author: k
"""
import cv2
image = cv2.imread("jurassic.png")
# grab the dimensions of the image and calculate the center
# of the image
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 180, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)