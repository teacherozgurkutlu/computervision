# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 00:46:21 2017

@author: k
"""
import cv2
 

image = cv2.imread("jurassic.png")
cv2.imshow("original", image)
# we need to keep in mind aspect ratio so the image does

#image.shape[0] resimin yüksekliğini verir
#image.shape[1] resimin genişliğini verir
# bu değerler kullnılarak resmin bozulmaması için oran belirleniyor
r=int(image.shape[0] * 300/image.shape[1]) #300 değeri istenen yeni genişliğin 
#değeri ile değiştirilmeli

dim = (300, r) # genişlik,yükseklik
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)