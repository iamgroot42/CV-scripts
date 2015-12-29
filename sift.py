import cv2
import numpy as np

img = cv2.imread('a.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
 
img=cv2.drawKeypoints(gray,kp)
cv2.imwrite('sift_keypoints.jpg',img)
cv2.waitKey(0)

# r = 800.0 / img.shape[1]
# dim = (800, int(img.shape[0] * r))
# resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
