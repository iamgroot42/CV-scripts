import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('a.jpg',0)
img2 = cv2.imread('b.jpg',0)

# Finding keypoints
# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create(80) #Try playing around with this
# find and draw the keypoints
kp = fast.detect(img,None)
lolk = cv2.drawKeypoints(img, kp,None)
kp2 = fast.detect(img2,None)
lolk2 = cv2.drawKeypoints(img2, kp,None)
# Print all default params
print "Keypoints in first image ", len(kp)
print "Keypoints in second image ", len(kp2)
cv2.imwrite('a_fast.png',lolk)
cv2.imwrite('b_fast.png',lolk2)

# Finding descriptors
# print dir(fast.compute().__doc__)
fast.compute(img,kp)
# print des
# brief = cv2.DescriptorExtractor_create("BRISK")
# brief = cv2.DescriptorExtractor_create("BRIEF")
# kp, des = brief.compute(img, kp)
# kp2, des2 = brief.compute(img2, kp2)
# print "Shape if first image ",des.shape