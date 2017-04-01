# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 00:40:07 2017

@author: k
"""
# import the necessary packages
import cv2
 
# load the image and show it
image = cv2.imread("jurassic.png")
cv2.imshow("original", image)
cv2.waitKey(0)
	
print image.shape #resimin boyutları consola yazdırılıyor
