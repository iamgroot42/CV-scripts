import numpy as np
import cv2

img_a = cv2.imread('pic_a.jpg',0)
img_b = cv2.imread('pic_b.jpg',0)

d2 = open('pts2d-pic_a.txt','r')
d3 = open('pts3d.txt','r')

d2_points = []
d3_points = []

for l in d2:
	l=l.rstrip()
	x,y = l.split('  ')
	d2_points.append((x,y,1))

d2_m = np.matrix(d2_points)

for l in d3:
	l=l.rstrip()
	x,y,z = l.split(' ')
	d3_points.append((x,y,z,1))

d3_m = np.matrix(d3_points)

# Use SVD to solve for M
# Calculate C as -inv(Q) * M(:,4)
# Inverse of matrix 
# np.linalg.inv(d3_m)