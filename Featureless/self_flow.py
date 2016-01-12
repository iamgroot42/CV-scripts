import numpy as np
import cv2
import sys

if len(sys.argv) < 3:
	print "Format : python feature_mapping.py <image1> <image2> "
	exit()

img = cv2.imread(sys.argv[1],0)
img2 = cv2.imread(sys.argv[2],0)

# img_vec = np.reshape(img,-1)
# img_vec2 = np.reshape(img2,-1)

Ix = np.zeros(img.shape)
Iy = np.zeros(img.shape)
It = np.zeros(img.shape)

Ix = 

# Continue from here