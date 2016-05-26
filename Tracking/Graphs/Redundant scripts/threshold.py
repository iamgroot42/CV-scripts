from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
from itertools import islice
import matplotlib.pyplot as plt
import numpy as np
import json
import Tkinter
import sys
import math
import csv
import os

rootdir = 'Values/'
inp1 = float(raw_input("Threshold for XX (50-100): "))
inp2 = float(raw_input("Threshold for YY (50-100): "))
inp1 = inp1/100
inp2 = inp2/100
d = set()
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		d.add(os.path.join(subdir))

d = sorted(d)
print d

dl = list(d)
ddict = {}
for i in dl:
	q1,q2 = os.path.split(i)
	if q1 in ddict:
		ddict[q1].append(i)
	else:
		q = []
		q.append(i)
		ddict[q1] = q

for yoho in ddict:
	all = []
	ky,kz = os.path.split(yoho)

	for x in ddict[yoho]:
		for subdir, dirs, files in os.walk(x):
			files.sort()
			for file in files:
				try:
					s = os.path.join(subdir,file)
					print s
					with open(s,'rw') as data_file:
						k = []
						k.append(file)
						all.append(k)
					   	data = json.load(data_file)
				except:
					print "I/O error"
					exit()

				keylist = data.keys()
				keylist.sort()
				top = []
				first = []
				top.append('-')
				first.append('Object')
				for p in keylist:
					first.append('YY')
					top.append(p)
					first.append('XX')
					top.append('-')
				all.append(top)
				all.append(first)

				for y in keylist:
					row = []
					row.append(y)
					val = data.get(y)
					for z in val:
						temp = []
						yy = z.get('YY')
						yx = z.get('YX')
						xx = z.get('XX')
						xy = z.get('XY')
						if yy >= inp2: 
							temp.append("1")
						elif yy < inp2:
							temp.append("0")
						if xx >= inp1: 
							temp.append("1")
						elif xx < inp1:
							temp.append("0")
						row = row + temp
					all.append(row)

			x1,x2 = os.path.split(x)
			b = x2+'_tab.csv'
			x3,x4 = os.path.split(x1)
			wayy = 'Outputs/'+kz+'/'
			if not os.path.exists(wayy):
    			os.makedirs(wayy)
			b = way+x4+b
			cw = open(b, 'w')
			rw = csv.writer(cw, lineterminator='\n')
			rw.writerows(all)
			cw.close()

	c = open(k)
	data = csv.reader(c)
	datal = list(data)
	row_count = len(datal)
	count = 0;
	c.seek(0)
	numcol = 0
	numrow = 0
	trow = []
	figl = []
	fig = (len(datal[1]) - 1)/2
	for i in range(1,fig+1):
		figl.append(i)

	check = [[0]*(fig+1) for _ in range(fig+1)]
	for i in range(1,fig+1):
		for j in range(i+1, fig+1):
			if j <= fig:
				st = "Enter 1/0 for "+str(i)+" and "+str(j)+" : "
				s = input(st)
				check[i][j] = s
	xtp = 0
	ytp = 0
	xfp = 0
	yfp = 0
	xtn = 0
	ytn = 0
	xfn = 0
	yfn = 0
	ctp = 0
	cfp = 0

	for i in range(2, 2+fig):
		for j in range((i*2)-1, (fig*2)+1):
			if(j<=(fig*2)):
				sec = (j+1)/2
				if check[i-1][sec]==1:
					if j%2==1:
						ytp = ytp + int(float(datal[i][j]))
					else:
						xtp = xtp + int(float(datal[i][j]))
					ctp = ctp + 1
				else:
					if j%2==1:
						yfp = yfp + int(float(datal[i][j]))
					else:
						xfp = xfp + int(float(datal[i][j]))
					cfp = cfp + 1


	cfp = cfp/2
	ctp = ctp/2

	first = int(float(datal[2][1]))
	xtn = (cfp*first) - xfp
	ytn = (cfp*first) - yfp
	xfn = (ctp*first) - xtp
	yfn = (ctp*first) - ytp

	print "True positive ",xtp,ytp
	print "True negative ",xtn,ytn
	print "False positive ",xfp,yfp
	print "False negative ",xfn,yfn

