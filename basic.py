import numpy as np
import cv2

img = cv2.imread('a.jpg',1)
img2 = cv2.imread('b.jpg',1)

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
# img = cv2.GaussianBlur(img,(7,7),0)

# Canny:
# img = cv2.Canny(img,img.min(),img.max())

# Resize image to fit screen 
# r = 800.0 / img.shape[1]
# dim = (800, int(img.shape[0] * r))
# resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# resized2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

# Harris corner detection 
# filename = 'a.jpg'
# img = cv2.imread(filename)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)

# #result is dilated for marking the corners, not important
# dst = cv2.dilate(dst,None)

# # Threshold for an optimal value, it may vary depending on the image.
# img[dst>0.01*dst.max()]=[0,0,255]

# Display images
# cv2.imshow('A',resized)
# cv2.imshow('B',resized2)
# cv2.waitKey(0)
