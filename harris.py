import cv2
import numpy as np

# Harris corner detection 
filename = 'a.jpg'
filename2 = 'b.jpg'
img = cv2.imread(filename)
img2 = cv2.imread(filename2)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
gray2 = np.float32(gray2)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst2 = cv2.cornerHarris(gray2,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
dst2 = cv2.dilate(dst2,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.05*dst.max()]=[0,0,255]
img2[dst2>0.05*dst2.max()]=[0,0,255]

r = 600.0 / img.shape[1]
dim = (600, int(img.shape[0] * r))
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
resized2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('A',resized)
cv2.imshow('B',resized2)
cv2.waitKey(0)