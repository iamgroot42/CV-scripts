import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("a.jpg")
img2 = cv2.imread("b.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
surf = cv2.xfeatures2d.SURF_create()
(kps, des) = surf.detectAndCompute(gray, None)
(kps2, des2) = surf.detectAndCompute(gray2, None)
print("A #  kps: {}, descriptors: {}".format(len(kps), des.shape))
print("B #  kps: {}, descriptors: {}".format(len(kps2), des2.shape))