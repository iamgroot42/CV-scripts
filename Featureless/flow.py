import numpy as np
import cv2
import sys

lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

if len(sys.argv) < 3:
	print "Format : python feature_mapping.py <image1> <image2> "
	exit()

img = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

flow = cv2.calcOpticalFlowFarneback(img_g,img_g2, None, 0.5, 3, 15, 3, 5, 1.2, 0)

hsv = np.zeros_like(img)
hsv[...,1] = 255

mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])

hsv[...,0] = ang*180/np.pi/2
hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imwrite('flow.jpg',bgr)