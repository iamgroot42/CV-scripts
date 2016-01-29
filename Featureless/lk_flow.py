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

def window_flow(window,window2,Ix=None,Iy=None):
	# Using the same A, as spatial derivatives remain the same
	It = np.zeros(window.shape)
	if Ix is None or Iy is None:
		Ix = cv2.Sobel(window,cv2.CV_64F,1,0,ksize=5)
		Iy = cv2.Sobel(window,cv2.CV_64F,0,1,ksize=5)

	It = window - window2
	Ix_Iy = np.sum(Ix*Iy)
	Ix_Ix = np.sum(np.square(Ix))
	Iy_Iy = np.sum(np.square(Iy))
	mat1 = np.matrix([[Ix_Ix,Ix_Iy],[Ix_Iy,Iy_Iy]])
	Ix_It = np.sum(Ix*It)
	Iy_It = np.sum(Iy*It)
	mat2 = np.matrix([[-Ix_It],[-Iy_It]])
	try:
		ans = np.linalg.inv(mat1) * mat2
	except:
		# Singular matrix - almost no motion
		ans = [0,0]
	return ans,Ix,Iy

def pyramid_transition(imag,imag2,initial,iters=10):
	iterations = 0
	u,v = initial
	M = np.float32([[1,0,u],[0,1,v]])
	imag = cv2.warpAffine(imag,M,(imag.shape[1],imag.shape[0]))
	temp = imag	
	while iterations < iters:
		# Calculating Ix,Iy for first iteration of this level
		if iterations is 0:	
			ret,Ix,Iy = window_flow(temp,imag2)
		else:
			ret = window_flow(temp,imag2,Ix,Iy)[0]
		u,v = u+ret[0],v+ret[1]
		M = np.float32([[1,0,u],[0,1,v]])
		# Warped original iamge by (u+del(u),v+del(v)) instead of warping new image by del(u),del(v)
		# , as rounding off errors keep accumulating 
  		temp = cv2.warpAffine(imag,M,(imag.shape[1],imag.shape[0]))
		iterations += 1
	#A drift of (u,v) becomes (2u,2v) for a level above it
	return [u*2,v*2] 


def pyramid(l1_1,l1_2):
	# Gaussian blur + downsample, to avoid aliasing
	kernel = np.ones((5,5),np.float32)/25
	l2_1,l2_2 = cv2.filter2D(l1_1,-1,kernel),cv2.filter2D(l1_2,-1,kernel)
	l2_1,l2_2 = l2_1[::2,::2],l2_2[::2,::2]
	l3_1,l3_2 = cv2.filter2D(l2_1,-1,kernel),cv2.filter2D(l2_2,-1,kernel)
	l3_1,l3_2 = l3_1[::2,::2],l3_2[::2,::2]
	l4_1,l4_2 = cv2.filter2D(l3_1,-1,kernel),cv2.filter2D(l3_2,-1,kernel)
	l4_1,l4_2 = l4_1[::2,::2],l4_2[::2,::2]
	l5_1,l5_2 = cv2.filter2D(l4_1,-1,kernel),cv2.filter2D(l4_2,-1,kernel)
	l5_1,l5_2 = l5_1[::2,::2],l5_2[::2,::2]
	x = [0,0]
	x = pyramid_transition(l5_1,l5_2,x)
	x = pyramid_transition(l4_1,l4_2,x)
	x = pyramid_transition(l3_1,l3_2,x)
	x = pyramid_transition(l2_1,l2_2,x)
	x = pyramid_transition(l1_1,l1_2,x)
	return [i for i in x]

print "Calculating flow..."
f_x,f_y = pyramid(img,img2)
print "Flow : ",f_x," , ",f_y