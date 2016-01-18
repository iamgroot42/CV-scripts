# Made by : Anshuman Suri

import numpy as np
import cv2
import sys

if len(sys.argv) < 3:
	print "Format : python self_flow.py <image1> <image2>"
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
	Ix[:,1:] = window[:,1:] - window[:,:-1]
	Iy[1:,] = window[1:,:] - window[-1:,:]
	It = window2 - window
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
		# Singular matrix : assuming negligible motion 
		ans = [0,0]
	return ans
		# u is along X axis,v is along Y axis

def pyramid_transition(imag,imag2,initial,iters=10):
	# print "Error",np.sum((imag-imag2)**2)
	iterations = 0
	u,v = initial
	while iterations < iters:
		# print "Error ",np.sum(np.square(imag-imag2))
		# Increasing error :|
		ret = window_flow(imag,imag2)
		u,v = u+ret[0],v+ret[1]
		print u,v
		temp = imag
		if(int(round(u))>0):
			temp[:,int(round(u)):] = imag[:,:-int(round(u))]
		elif(int(round(u))<0):
			temp[:,:int(round(u))] = imag[:,-int(round(u)):]
		if(int(round(v))>0):
			temp[int(round(v)):,:] = imag[:-int(round(v)),:]
		elif(int(round(v))<0):
			temp[:int(round(v)),:] = imag[-int(round(v)):,:]
		imag = temp
		cv2.imwrite('Harish/'+str(u)+'.jpg',temp)
		# print "Error",np.sum((imag-imag2)**2)
		iterations += 1
	return [u*2,v*2] #A drift of (u,v) becomes (2u,2v) for a level above it


def pyramid(l1_1,l1_2):
	l2_1,l2_2 = l1_1[::2,::2],l1_2[::2,::2]
	l3_1,l3_2 = l2_1[::2,::2],l2_2[::2,::2]
	l4_1,l4_2 = l3_1[::2,::2],l3_2[::2,::2]
	l5_1,l5_2 = l4_1[::2,::2],l4_2[::2,::2]
	x = [0,0]
	x = pyramid_transition(l5_1,l5_2,x)
	# print "Level change :)"
	x = pyramid_transition(l4_1,l4_2,x)
	# print "Level change :)"
	x = pyramid_transition(l3_1,l3_2,x)
	# print "Level change :)"
	x = pyramid_transition(l2_1,l2_2,x)
	# print "Level change :)"
	x = pyramid_transition(l1_1,l1_2,x)
	return [i/2 for i in x]

# Main :
f_x,f_y = pyramid(img,img2)	
print "Flow is ",f_x," , ",f_y
print "Naive ",window_flow(img,img2)