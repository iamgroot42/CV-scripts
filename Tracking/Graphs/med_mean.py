import json
import matplotlib.pyplot as plt
import numpy as np
import Tkinter
import sys
from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
import math
import csv
from itertools import islice
import sys
import os

rootdir = 'Outputs/'
d = set()
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		k = os.path.join(subdir, file)
		c = open(k)
		data = csv.reader(c)
		datal = list(data)
		row_count = len(datal)
		# print row_count
		count = 0;
		c.seek(0)
		numcol = 0
		numrow = 0
		trow = []
		for i in data:
			if count == 2:
				trow = i
				numcol = len(i)
				numrow = (numcol-1)/2
				rowtemp = numrow
				# print numcol
			count += 1
		c.seek(0)
		all = []
		allm = []
		row_flag = 3
		tempc=[]
		tempr = []
		temprm = []
		tempcm =[]
		for x in range(0,numrow):
			tempr = []
			temprm = []
			for y in range(1, numcol):
				c.seek(0)
				count = 0
				tempc = []
				tempcm = []
				for i in data:
					# print i
					if (count-row_flag)%(rowtemp+3)==0:
						# print i
						tempc.append(i[y])
						tempcm.append(i[y])
					count = count+1
				r = map(float, tempc)
				rm = map(float, tempcm)
				q = np.mean(r)
				qm = np.median(rm)
				tempr.append(q)
				temprm.append(qm)
			tempr = [str(x+1)] + tempr
			temprm = [str(x+1)] + temprm
			all.append(tempr)
			allm.append(temprm)
			row_flag += 1
		alls = []
		alls.append(['mean'])
		alls.append(trow)
		for g in all:
			alls.append(g)
		alls.append([])
		alls.append(['median'])
		alls.append(trow)
		for g in allm:
			alls.append(g)

		c.close()
		x1,x2 = os.path.split(k)
		b = os.path.splitext(x2)[0]
		b = 'Final/'+b+'med_mean.csv'
		print b
		cw = open(b,'w')
		rw = csv.writer(cw, lineterminator='\n')
		rw.writerows(alls)
		cw.close()







# She wanted only the sparkle of his eyes,
# He promised her to bring the stars of skies,
# With another promise she was again left out,
# Words worked again, the evil inside him said aloud