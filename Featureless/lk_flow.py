# Made by : Anshuman Suri

import numpy as np
import cv2
import sys

if len(sys.argv) < 3:
	print "Format : python "+sys.argv[0]+" <image1> <image2>"
	exit()

try:
	img_in = cv2.imread(sys.argv[1])
	img2_in = cv2.imread(sys.argv[2])
except:
	print "I/O error"
	exit()

img = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2_in, cv2.COLOR_BGR2GRAY)

def window_flow(window,window2):
	Ix = np.zeros(window.shape)
	Iy = np.zeros(window.shape)
	It = np.zeros(window.shape)
	Ix = cv2.Sobel(window,cv2.CV_64F,1,0,ksize=5)
	Iy = cv2.Sobel(window,cv2.CV_64F,0,1,ksize=5)
	It = window - window2

	A_a = np.matrix(Ix.ravel())
	A_b = np.matrix(Iy.ravel())
	A = np.vstack((A_a,A_b))
	A = np.transpose(A)
	B = np.matrix(It.ravel())
	B = np.transpose(B)
	answer = np.linalg.lstsq(A, B)[0]
	return answer

def pyramid_transition(imag,imag2,initial,iters=30):
	# print "Error",np.sum((imag-imag2)**2)
	iterations = 0
	u,v = initial

	M = np.float32([[1,0,round(u)],[0,1,round(v)]])
	imag = cv2.warpAffine(imag,M,(imag.shape[1],imag.shape[0]))
	temp = imag

	while iterations < iters:
		error = np.sum(np.square(temp-imag2))
		# print "Error ",error
		ret = window_flow(temp,imag2)
		u,v = u+ret[0],v+ret[1]
		M = np.float32([[1,0,round(u)],[0,1,round(v)]])
		# Warped original iamge by (u+del(u),v+del(v)) instead of warping new image by del(u),del(v)
		# ,as rounding off errors keep accumulating 
  		temp = cv2.warpAffine(imag,M,(imag.shape[1],imag.shape[0]))
  		# try:
		# 	cv2.imwrite('Harish/'+str(u)+'.jpg',imag)
		# except:
		# 	print "I/O error"
		iterations += 1
	return [u*2,v*2] #A drift of (u,v) becomes (2u,2v) for a level above it


def pyramid(l1_1,l1_2):
	l2_1,l2_2 = l1_1[::2,::2],l1_2[::2,::2]
	l3_1,l3_2 = l2_1[::2,::2],l2_2[::2,::2]
	l4_1,l4_2 = l3_1[::2,::2],l3_2[::2,::2]
	l5_1,l5_2 = l4_1[::2,::2],l4_2[::2,::2]	
	x = [0,0]
	x = pyramid_transition(l5_1,l5_2,x)
	x = pyramid_transition(l4_1,l4_2,x)
	x = pyramid_transition(l3_1,l3_2,x)
	x = pyramid_transition(l2_1,l2_2,x)
	x = pyramid_transition(l1_1,l1_2,x)
	return [i/2 for i in x]

# Main :
print "Calculating flow..."
f_x,f_y = pyramid(img,img2)	
print "Flow : ",f_x," , ",f_y
naive = window_flow(img,img2)
print "Flow (naive) : ",naive[0]," ",naive[1]