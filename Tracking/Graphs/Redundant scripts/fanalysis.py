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

k = raw_input("Enter file path: ")
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




# for i in data:
# 	if count == 2:
# 		trow = i
# 		numcol = len(i)
# 		numrow = (numcol-1)/2
# 		rowtemp = numrow
# 	count += 1
# c.seek(0)
# all = []
# allm = []
# row_flag = 3
# tempc=[]
# tempr = []
# temprm = []
# tempcm =[]
# for x in range(0,numrow):
# 	tempr = []
# 	temprm = []
# 	for y in range(1, numcol):
# 		c.seek(0)
# 		count = 0
# 		tempc = []
# 		tempcm = []
# 		for i in data:
# 			if (count-row_flag)%(rowtemp+3)==0:
# 				tempc.append(i[y])
# 				tempcm.append(i[y])
# 			count = count+1
# 		r = map(float, tempc)
# 		rm = map(float, tempcm)
# 		q = np.sum(r)
# 		qm = np.median(rm)
# 		tempr.append(q)
# 		temprm.append(qm)
# 	tempr = [str(x+1)] + tempr
# 	temprm = [str(x+1)] + temprm
# 	all.append(tempr)
# 	allm.append(temprm)
# 	row_flag += 1
# alls = []
# alls.append([k])
# alls.append(trow)
# for g in all:
# 	alls.append(g)
# # alls.append([])
# # alls.append(['median'])
# # alls.append(trow)
# # for g in allm:
# # 	alls.append(g)

c.close()
# x1,x2 = os.path.split(k)
# b = os.path.splitext(x2)[0]
# b = 'sumvalues.csv'
# print b
# cw = open(b,'w')
# rw = csv.writer(cw, lineterminator='\n')
# rw.writerows(alls)
# cw.close()
