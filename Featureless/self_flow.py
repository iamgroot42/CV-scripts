import numpy as np
import cv2
import sys

if len(sys.argv) < 3:
	print "Format : python feature_mapping.py <image1> <image2> "
	exit()

img = cv2.imread(sys.argv[1],0)
img2 = cv2.imread(sys.argv[2],0)

def window_flow(window,window2):
	Ix = np.zeros(window.shape)
	Iy = np.zeros(window.shape)
	It = np.zeros(window.shape)
	Ix[:,1:] = window[:,1:] - window[:,:-1]
	Iy[1:,] = window[1:,] - window[-1,]
	It[:,:] = window[:,:] - window2[:]
	Ix_Ix = np.sum(np.square(Ix))
	Iy_Iy = np.sum(np.square(Iy))
	Ix_Iy = np.sum(Ix*Iy)
	Ix_It = np.sum(Ix*It)
	Iy_It = np.sum(Iy*It)

	mat1 = np.matrix([[Ix_Ix,Ix_Iy],[Ix_Iy,Iy_Iy]])
	mat2 = np.matrix([[-Ix_It],[-Iy_It]])

	try:
		ans = np.linalg.inv(mat1) * mat2
	except:
		# Singular matrix : so almost no motion in this part
		ans = [0,0]
	return ans

r,c = img.shape[:2]

i=0
j=0

flow_x = np.zeros((r/5,c/5))
flow_y = np.zeros((r/5,c/5))

for i in range(r/5):
	for j in range(c/5):
		flow_x[i,j],flow_y[i,j] = window_flow(img[5*i:5*i+5,5*j:5*j+5],img2[5*i:5*i+5,5*j:5*j+5])

print "Horizontal flow"
print flow_x
print "Vertical flow"
print flow_y