import json
import matplotlib.pyplot as plt
import numpy as np
import Tkinter
import sys
from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
import math


if len(sys.argv) < 2:
	print "python " + sys.argv[0] + " file_name (.json file)"
	exit()
else:
	file_name = sys.argv[1]

try:
    with open(file_name) as data_file:
    	data = json.load(data_file)
except:
	print "I/O error"
	exit()

# Arrange frames chronologically
frames = sorted(data, key=itemgetter('time'))

nPeople = len(frames[0]['data'])
time = 1

X = []
Y = []
Z = []
E = []


# Sort by y-coordinate to approximate which user is which in the next frame. Not the
# best way to do it, but works for the given dataset
for frame in frames:
	faces = sorted(frame['data'], key=itemgetter('y'))
	xdiff = faces[0].get('x') - faces[1].get('x')
	ydiff = faces[0].get('y') - faces[1].get('y')
	euc_diff = math.sqrt(math.pow(xdiff,2)+math.pow(ydiff,2))
	X.append(xdiff)
	Y.append(ydiff)
	Z.append(time)
	E.append(euc_diff)
	time += 1

zer = [0 for x in range(time-1)]

plt.plot(Z,X,color='r', label ='X Difference')
plt.plot(Z,Y,color='b', label ='Y Difference')
plt.plot(Z,E,color='g', label ='Euclidean Difference')
plt.plot(Z,zer, color='black')

plt.title('Value differences between two faces')
plt.xlabel('Frame Number')
plt.ylabel('Value differences')
plt.legend()
plt.show()
