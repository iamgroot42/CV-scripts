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

A = [] # (2n,9) matrix
for i in range(p.shape[0]): 
	x1,y1 = float(p.item(i+0)),float(p.item(i+1))
	x2,y2 = float(p2.item(i+0)),float(p2.item(i+1))
	_x2 = -float(x2)
	_y2 = -float(y2)
	A.append([_x2,_y2,-1,0,0,0,x2*x1,x1*y2,x1])
	A.append([0,0,0,_x2,_y2,-1,y1*x2,y2*y1,y1])
A = np.matrix(A)
zeroes = np.zeros(A.shape[0])

# SVD solution 
u,s,v = np.linalg.svd(A,True,True)
# A = u.s.v , we need last column of v' , that is, last row of v
Hs = v[v.shape[0]-1:].reshape(3,3)
for i in range(9):
	Hs[i/3,i%3]/=Hs[2,2]
print "Homography matrix (SVD) : "	
print Hs

# pot = Hs * np.matrix([[1],[2],[1]])
# print pot.item(0)/pot.item(2)
# print pot.item(1)/pot.item(2)

print "Inverse Homography matrix (SVD) : "
Hsinv = np.linalg.inv(Hs)
for i in range(9):
	Hsinv[i/3,i%3]/=Hsinv[2,2]
print Hsinv