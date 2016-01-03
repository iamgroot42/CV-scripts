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
	x1,y1 = float(p.item(i+0)),float(p.item(i+1))
	x2,y2 = float(p2.item(i+0)),float(p2.item(i+1))
	_x2 = -float(x2)
	_y2 = -float(y2)
	A.append([0,0,0,_x2,_y2,-1,float(x2)*float(y1),float(y2)*float(y1),y1])
	A.append([x2,y2,1,0,0,0,float(_x2)*float(x1),float(_y2)*float(x1),-float(x1)])
	A.append([float(_x2)*float(y1),float(_y2)*float(y1),-float(y1),float(x2)*float(x1),float(y2)*float(x1),x1,0,0,0])
A = np.matrix(A)
zeroes = np.zeros(A.shape[0])

H = np.linalg.lstsq(A, zeroes)[3]

for i in range(9):
	H[i]/=H[8]

# Least square solution
# matr = H.reshape((3,3))
# print "Homography matrix (least square) : "
# print matr
# print "Inverse homography (least square) : "
# Hinv = np.linalg.inv(matr) 
# for i in range(9):
# 	Hinv[i/3,i%3]/=Hinv[2,2]
# print Hinv
# print ""

# SVD solution 
print "Homography matrix (SVD) : "
u,s,v = np.linalg.svd(A,True,True)
Hs = v[v.shape[0]-1:].reshape(3,3)
for i in range(9):
	Hs[i/3,i%3]/=Hs[2,2]
print Hs
print "Inverse Homography matrix (SVD) : "
Hsinv = np.linalg.inv(Hs)
for i in range(9):
	Hsinv[i/3,i%3]/=Hsinv[2,2]
print Hsinv