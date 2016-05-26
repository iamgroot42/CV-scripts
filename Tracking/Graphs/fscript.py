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
inpx = input("Threshold for XX (50-100): ")
inpy = input("Threshold for YY (50-100): ")
inp1 = float(inpx)*(1.0)/100
inp2 = float(inpy)*(1.0)/100
d = set()
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		d.add(os.path.join(subdir))

d = sorted(d)
# print d

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

# head = ['Filename','TruePos_X','TruePos_Y','TrueNeg_X','TrueNeg_Y','FalsePos_X','FalsePos_Y','FalseNg_X','FalseNeg_Y']
head = ['Filename','Precision_X','Accuracy_X','Recall_X','Precision_Y','Accuracy_Y','Recall_Y']
for yoho in ddict:
	all = []
	ky,kz = os.path.split(yoho)
	wayy = 'Outputs/'+kz+'/'	
	print '\n'
	for x in ddict[yoho]:
		for subdir, dirs, files in os.walk(x):
			files.sort()
			all = []
			for file in files:
				try:
					s = os.path.join(subdir,file)
					# print s
					# all = []
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
			rt = 'Outputs/'+x4+b
			cw = open(rt, 'w')
			# print rt
			rw = csv.writer(cw, lineterminator='\n')
			rw.writerows(all)
			cw.close()


			c = open(rt)
			data = csv.reader(c)
			datal = all
			row_count = len(datal)
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
						if (count-row_flag)%(rowtemp+3)==0:
							# print "y ",y
							tempc.append(i[y])
							tempcm.append(i[y])
						count = count+1
					r = map(float, tempc)
					rm = map(float, tempcm)
					q = np.sum(r)
					qm = np.median(rm)
					tempr.append(q)
					temprm.append(qm)
				tempr = [str(x+1)] + tempr
				temprm = [str(x+1)] + temprm
				all.append(tempr)
				allm.append(temprm)
				row_flag += 1
			alls = []
			alls.append([rt])
			alls.append(trow)
			# print "trow ",trow
			for g in all:
				alls.append(g)

			c.close()
			gh = x2+'_sums.csv'
			if not os.path.exists(wayy):
				os.makedirs(wayy)
			gh = wayy+x4+gh
			cw = open(gh, 'w')
			# print gh
			rw = csv.writer(cw, lineterminator='\n')
			rw.writerows(alls)
			cw.close()


	for subdir, dirs, files in os.walk(wayy):
			files.sort()
			check1 = [[]]
			fc = 10
			for file in files:
				# try:
				# fc = 10
				s4 = os.path.join(subdir,file)
				# print s
				all = []
				c4 = open(s4)
				data4 = csv.reader(c4)
				datal4 = list(data4)
				row_count = len(datal4)
				count = 0;
				c4.seek(0)
				numcol = 0
				numrow = 0
				trow = []
				figl = []
				fig = (len(datal[1]) - 1)/2
				for i in range(1,fig+1):
					figl.append(i)

				if fc==10:
					print "file is ",yoho
					check = [[0]*(fig+1) for _ in range(fig+1)]
					for i in range(1,fig+1):
						for j in range(i+1, fig+1):
							if j <= fig:
								st = "Enter 1/0 for "+str(i)+" and "+str(j)+" : "
								s2 = input(st)
								check[i][j] = s2
								# print "dhdbhj "
					check1 = check

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
							if check1[i-1][sec]==1:
								if j%2==1:
									ytp = ytp + int(float(datal4[i][j]))
								else:
									xtp = xtp + int(float(datal4[i][j]))
								ctp = ctp + 1
							else:
								if j%2==1:
									yfp = yfp + int(float(datal4[i][j]))
								else:
									xfp = xfp + int(float(datal4[i][j]))
								cfp = cfp + 1


				cfp = cfp/2
				ctp = ctp/2

				first = int(float(datal4[2][1]))
				xtn = (cfp*first) - xfp
				ytn = (cfp*first) - yfp
				xfn = (ctp*first) - xtp
				yfn = (ctp*first) - ytp
				# print "h"
				lola = 'My_Analysis/'+str(inpx)+'_'+str(inpy)+'/'
				app = []
				app.append(head)
				if not os.path.exists(lola):
					os.makedirs(lola)
					for yr in range(1,5):
						fk = lola+'analysis_'+str(yr)+'0.csv'
						op1 = open(fk, 'w')
						op2 = csv.writer(op1, lineterminator='\n')
						op2.writerows(app)
						op1.close()

				# print s4
				nopr = []
				fk = lola+'analysis_'+str(fc)+'.csv'
				tok = open(fk)
				da1 = csv.reader(tok)
				# da2 = list(da1)
				for kf in da1:
					nopr.append(kf)
				x_precision = xtp/float(xtp+xfp)
				x_accuracy = (xtp + xtn)/float(xtp + xtn + xfp + xfn)
				x_recall = xtp/float(xtp+xfn)
				y_precision = ytp/float(ytp+yfp)
				y_accuracy = (ytp + ytn)/float(ytp + ytn + yfp + yfn)
				y_recall = ytp/float(ytp+xfn)
				accha = [yoho,x_precision,x_accuracy,x_recall,y_precision,y_accuracy,y_recall]
				nopr.append(accha)
				tok.close()
				tok = open(fk, 'w')
				tok2 = csv.writer(tok, lineterminator='\n')
				tok2.writerows(nopr)
				tok.close()
				# print "True positive ",xtp,ytp
				# print "True negative ",xtn,ytn
				# print "False positive ",xfp,yfp
				# print "False negative ",xfn,yfn
				# print fk
				# print "\n"
				fc = fc + 10

				# except:
				# 	print "I/O error"
				# 	exit()
	

