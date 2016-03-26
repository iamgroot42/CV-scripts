import json
import matplotlib.pyplot as plt
import numpy as np
import Tkinter
from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

colors = ['DarkMagenta','Blue','Yellow']

with open('Graphs/points.json') as data_file:    
    data = json.load(data_file)

# Arrange frames chronologically
frames = sorted(data, key=itemgetter('time'))

nPeople = len(frames[0]['data'])
time = 1

X = [[] for x in range(nPeople)]
Y = [[] for x in range(nPeople)]
Z = []

# Sort by y-coordinate to approximate which user is which in the next frame. Not the
# best way to do it, but works for the given dataset
for frame in frames:
	faces = sorted(frame['data'], key=itemgetter('y'))
	for i in range(nPeople):
		X[i].append(faces[i].get('x'))
		Y[i].append(faces[i].get('y'))
	Z.append(time)
	time += 1

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plotting coordinates for every tracked person
for i in range(nPeople):
	ax.plot(X[i],Y[i],Z,label = str(i+1), color = colors[i], linewidth = 3.2)
	print "alele"

rcParams['legend.fontsize'] = 11
ax.legend()

ax.set_xlabel('X axis')
ax.set_xlim(0,1000)
ax.set_ylabel('Y axis')
ax.set_ylim(0,1000)
ax.set_zlabel('Time (s)')
ax.set_zlim(0,40)

ax.set_title('Face Tracking', va='bottom')
ax.view_init(elev=18, azim=-27)
ax.dist=9
plt.show()
