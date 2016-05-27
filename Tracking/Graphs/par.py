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


rootdir = 'My_Analysis/'
for subdir, dirs, files in os.walk(rootdir):
	files.sort()
	all = []
	for file in files:
		try:
			all = []
			s = os.path.join(subdir,file)
			print s
			tok = open(s)
			da1 = csv.reader(tok)
			# da2 = list(da1)
			for kf in da1:
				fg = []
				for gf in range(0,9):
					fg.append(kf[gf])
				all.append(fg)
			head = ['','Precision_X','Accuracy_X','Recall_X','Precision_Y','Accuracy_Y','Recall_Y']
			for h in head:
				all[0].append(h)
			alen = len(all)
			for i in range(1,alen):
				xtp = int(all[i][1])
				ytp = int(all[i][2])
				xtn = int(all[i][3])
				ytn = int(all[i][4])
				xfp = int(all[i][5])
				yfp = int(all[i][6])
				xfn = int(all[i][7])
				yfn = int(all[i][8])
				if xtp+xfp==0:
					x_precision = 1
				else:
					x_precision = xtp/float(xtp+xfp)

				if xtp + xtn + xfp + xfn==0:
					x_accuracy = 1
				else:
					x_accuracy = (xtp + xtn)/float(xtp + xtn + xfp + xfn)

				if xtp+xfn==0:
					x_recall = 1
				else:
					x_recall = xtp/float(xtp+xfn)

				if ytp+yfp==0:
					y_precision = 1
				else:
					y_precision = ytp/float(ytp+yfp)

				if ytp + ytn + yfp + yfn==0:
					y_accuracy = 1
				else:
					y_accuracy = (ytp + ytn)/float(ytp + ytn + yfp + yfn)

				if ytp+yfn==0:
					y_recall = 1
				else:
					y_recall = ytp/float(ytp+yfn)

				accha1 = ['',x_precision,x_accuracy,x_recall,y_precision,y_accuracy,y_recall]
				for g in accha1:
					all[i].append(g)
				tok.close()
				tok = open(s, 'w')
				tok2 = csv.writer(tok, lineterminator='\n')
				print accha1
				print
				tok2.writerows(all)
				tok.close()

			# all = []
			
		except:
			print "I/O error"
			exit()