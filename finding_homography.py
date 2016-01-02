import numpy as np
import cv2

try:
	fp = open('points_img1.txt','r')
	fp2 = open('points_img2.txt','r')
except:
	print "Files not found.Run 'features.py' first"
	exit()

p = []
p2 = []

for line in fp:
	x,y = line.rstrip().split(' ')
	p.append((x,y))

for line in fp2:
	x,y = line.rstrip().split(' ')
	p2.append((x,y))

p = np.matrix(p)
p2 = np.matrix(p2)

A = [] # (3n,9) matrix
for i in range(p.shape[0]): 
	x1,y1 = p.item(i+0),p.item(i+1)
	x2,y2 = p2.item(i+0),p2.item(i+1)
	_x1 = -float(x1)
	_y1 = -float(y1)
	A.append((x2,y2,1,0,0,0,0,0,_x1))
	A.append((0,0,0,x2,y2,1,0,0,_y1))
	A.append((0,0,0,0,0,0,x2,y2,0))

A = np.matrix(A)
zeroes = np.zeros(A.shape[0])

H = np.linalg.lstsq(A, zeroes)[3]

for i in range(9):
	H[i]/=H[8]

#Make square matrix
matr = H.reshape((3,3))
print "Homography matrix : "
print matr