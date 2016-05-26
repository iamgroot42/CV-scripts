import json
import numpy as np
import sys
from operator import itemgetter
import matplotlib.pyplot as plt


# Correlation
def corr(A, B, pop):
	rekt = {}
	for j in range(pop):
		ret = []
		for k in range(pop):
			p = [x[j] for x in A]
			q = [x[k] for x in A]
			r = [y[j] for y in B]
			s = [y[k] for y in B]
			ret.append({"XX":np.corrcoef(p,q)[0][1],"YY":np.corrcoef(r,s)[0][1]})
		rekt[str(j+1)]=ret
	return rekt
	

# Sliding window
def slider(A, B, ws, pop):
	windowA = A[:ws]
	windowB = B[:ws]
	L = len(A)
	corr(windowA,windowB,pop)
	for i in range(L-ws):
		tbw = corr(windowA, windowB, pop)
		f = open("Values/"+str(i+1)+".txt",'w')
		json.dump(tbw,f)
		windowA.append(A[ws+i])
		windowA = windowA[1:]
		windowB.append(B[ws+i])
		windowB = windowB[1:]


# Main function 	
def all_corr(data, window_size):
	# Arrange frames chronologically
	frames = sorted(data, key=itemgetter('time'))

	nframes = len(frames)
	nPeople = len(frames[0]['data'])
	j = 0

	X = [[] for x in range(nframes)]
	Y = [[] for x in range(nframes)]

	# Sort by x-coordinate to approximate which user is which in the next frame. Not the
	# best way to do it, but works
	for frame in frames:
		faces = sorted(frame['data'], key=itemgetter('x'))
		for i in range(nPeople):
			X[j].append(faces[i].get('x'))
			Y[j].append(faces[i].get('y'))
		j += 1
	slider(X, Y, window_size, nPeople)



if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "python " + sys.argv[0] + " file_name(.json file) <window_size>"
		exit()
	else:
		file_name = sys.argv[1]
		window_size = int(sys.argv[2])

	try:	
	    with open(file_name) as data_file:
    		data = json.load(data_file)
	except:
		print "I/O error"
		exit()
	all_corr(data, window_size)
