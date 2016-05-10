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

rootdir = 'Values/'
inp1 = float(raw_input("Threshold for XX: "))
inp2 = float(raw_input("Threshold for YY: "))
d = set()
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		d.add(os.path.join(subdir))

d = sorted(d)
dl = list(d)
for x in dl:
	all = []
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
				# first.append('YX')
				# top.append('-')
				first.append('XX')
				top.append('-')
				# first.append('XY')
				# top.append('-')
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
					# temp.append(yy)
					# temp.append(yx)
					# temp.append(xx)
					# temp.append(xy)
					row = row + temp
				all.append(row)
			# temp=[]
			# all.append(temp)

		x1,x2 = os.path.split(x)
		b = x2+'_tabanalysis.csv'
		x3,x4 = os.path.split(x1)
		b = 'Analysis/' +x4+b
		cw = open(b, 'w')
		rw = csv.writer(cw, lineterminator='\n')
		rw.writerows(all)
		cw.close()






