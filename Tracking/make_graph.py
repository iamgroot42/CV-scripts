import json
from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
import Tkinter


with open('Graphs/points.json') as data_file:    
    data = json.load(data_file)

d = sorted(data, key=itemgetter('time'))

x1 = []
y1 = []
x2 = []
y2 = []
z = []
time = 1

for e in d:
	faces = sorted(e['data'], key=itemgetter('y'))
	y1.append(faces[0].get('y'))
	y2.append(faces[1].get('y'))
	x1.append(faces[0].get('x'))
	x2.append(faces[1].get('x'))
	z.append(time)
	time += 1

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1,y1,z,label = 'Tracking1', color = 'DarkMagenta', linewidth = 3.2,)
ax.plot(x2,y2,z,label = 'Tracking2', color = 'Green', linewidth = 3.2,)
rcParams['legend.fontsize'] = 11
ax.legend()

ax.set_xlabel('X axis')
ax.set_xlim(0,1000)
ax.set_ylabel('Y axis')
ax.set_ylim(0,1000)
ax.set_zlabel('Time')
ax.set_zlim(0,40)

ax.set_title('3D line plot, \n Face Tracking', va='bottom')
ax.view_init(elev=18, azim=-27)
ax.dist=9
plt.show()

	