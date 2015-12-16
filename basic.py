import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('house.tiff',1)
img2 = cv2.imread('jelly.tiff',1)
b,g,r = cv2.split(img)
# Or :
# b=img[:,:,0]
# g=img[:,:,1]
# r=img[:,:,2]
alpha = 0.29
x = cv2.addWeighted(img,alpha,img2,1-alpha,0)
cv2.imshow('Jelly+House',x)
cv2.waitKey(0)
# cv2.destroyAllWindows()