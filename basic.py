import numpy as np
import cv2

img = cv2.imread('coins.png',0)

# b,g,r = cv2.split(img)
# Or
# b=img[:,:,0]
# g=img[:,:,1]
# r=img[:,:,2]

# alpha = 0.29
# x = cv2.addWeighted(img,alpha,img2,1-alpha,0)

# Swapping R/B channels:
# img[:,:,2],img[:,:,0]=img[:,:,0],img[:,:,2]
# img-=img.mean()
# img=(img)/(2*img.std())

# Blur
# img = cv2.blur(img,(15,15))

# Median Blur
# img = cv2.medianBlur(img,5)

# Bilateral Filter
# img = cv2.bilateralFilter(img,9,75,75)

# Gaussian Blur 
img = cv2.GaussianBlur(img,(7,7),0)

# Canny:
img = cv2.Canny(img,img.min(),img.max())

cv2.imshow('Modern Art',img)
cv2.waitKey(0)