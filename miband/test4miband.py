'''
Created on 10/2015

@author: fan03d

Run example: python test4miband.py data
'''
import csv
import sys
import numpy as np
from sklearn.naive_bayes import GaussianNB
import itertools
from sklearn.metrics import confusion_matrix

def runMaxVal(fdata):
	print 'Run Maximal Value Algorithm ..'

	alldata=[]

	X=[]
	Y=[]
	with open(fdata, 'rb') as f:
		reader=csv.reader(f)
		index =0
		for row in reader:
			
			alldata.append(row)
			xrow=[]
			for i in range(1,9):
				xrow.append(float(row[i]))
			
			X.append(xrow)	
			Y.append(int(row[len(row)-1]))

	pred_Y=[]
	corr =0
	total =0
	for xrow, yrow in zip(X, Y):
		total = total +1
		curi=0
		curval = -200
		pred=0
		for xi in xrow:
			if xi > curval:
				pred = curi
				curval =xi

			curi = curi +1 	
	
		pred_Y.append(pred)
		if pred == yrow:
			corr =corr +1

	print 'Accuracy ',corr*1.0/total	
	
	print 'confusion matrix'
	cm=confusion_matrix(Y,pred_Y)
	cm_norm = cm*1./cm.sum(axis=1)

	print cm_norm


def runHistogram(fdata):
	print 'Run NB-Histogram ..'
	alldata=[]
	
	X=[]
	Y=[]

	with open(fdata, 'rb') as f:
		reader=csv.reader(f)
		index =0
		for row in reader:
			
			alldata.append(row)
			xrow=[]
			for i in range(1,9):
				sigval = float(row[i])
				if sigval > -10:
					xrow.append(0)
				elif sigval >-20:
					xrow.append(1)
				elif sigval > -30:
					xrow.append(2)
				elif sigval > -40:
					xrow.append(3)
				elif sigval > -50:
					xrow.append(4)
				elif sigval > -60:
					xrow.append(5)
				elif sigval > -70:
					xrow.append(6)
				elif sigval > -80:
					xrow.append(7)
				elif sigval > -90:
					xrow.append(8)
				elif sigval >-100:
					xrow.append(9)
				elif sigval >-110:
					xrow.append(10)
				else:
					xrow.append(11)
	
			X.append(xrow)	
			Y.append(int(row[len(row)-1]))
	
	prior=np.array([0,0,0,0,0,0,0,0])
	
	for yi in Y:
		prior[yi] = prior[yi]+1
	
	prior=prior*1./len(Y)
	
	likelihood=[]
	for i in range(8):
		tmp=[]
		for j in range(12):
			tmp.append([0,0,0,0,0,0,0,0])
	
		likelihood.append(tmp)
	
	
	for xvec, yi in zip(X,Y):
			i=0
			for xi in xvec:
				likelihood[i][xi][yi] += 1
				i+=1
				
	likelihood = np.array(likelihood)

	
	corr =0
	total =0
	corr_all=[0,0,0,0,0,0,0,0]
	total_all=[0,0,0,0,0,0,0,0]
	
	pred_y=[]
	
	for xvec, true_y in zip(X,Y):
		total +=1
		predval=0.
		maxpred=0.
		maxlabel=0
		for label_y in range(8):
			predval=prior[label_y]
			for var in range(8):
				predval=predval*likelihood[var][xvec[var]][label_y]
			
			if predval > maxpred:
				maxpred= predval
				maxlabel = label_y
		
		total_all[true_y] +=1
		pred_y.append(maxlabel)
		if maxlabel == true_y:
			corr +=1
			corr_all[true_y] +=1
	
	print 'Accuracy ', corr*1./total	
	print 'confusion matrix'
	cm=confusion_matrix(Y,pred_y)
	cm_norm = cm*1./cm.sum(axis=1)
	print cm_norm
	

if __name__=="__main__":

	fdata = sys.argv[1]

	runMaxVal(fdata)
	runHistogram(fdata)
