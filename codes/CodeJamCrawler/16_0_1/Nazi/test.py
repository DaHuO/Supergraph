

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats
from sklearn.cross_validation import KFold
from pylab import *
from sklearn import datasets, linear_model
import timeit
import math
import warnings
warnings.filterwarnings('ignore')

# Reading files
def readFile(filename):
	with open(filename, "r") as f:
		x = [] 
		y = []
		col = 2
		rows = 0
		for line in f:
			numbers = line.split()
			if (numbers[0]=="#" and numbers[1][0]=="c" and numbers[1][1]=="o" ):
				col = numbers[2]
				col = int(col)

			if (numbers[0]=="#" and numbers[1][0]=="r"):
				rows = numbers[2]
				rows = int(rows)
 
			if (numbers[0]!="#"):
				tmp = []
				for i in range(0,col-1):
					tmp.append(numbers[i])
				x.append(tmp)
				y.append(numbers[col-1])

	x = np.array(x)
	x = x.astype(np.float)
	y = np.array(y)
	y = y.astype(np.float)
	return x,y,rows

# Gaussian kernel function
def gauss(x,y,sigma):
	k=0
	for i in range(0,len(x)):
		k = k + (x[i]-y[i])**2
	k = exp((-1/(2*sigma))*k)
	return k

# Finding theta using an iterative solution
def regIterative(z,y,n,err):
	w_old=np.ones(len(z[0]))
	w_new=0
	p=0
	for j in range(0,err):
		sum = 0
		for i in range(0,len(z)):
			sum = sum + (inner(w_old,z[i])-y[i])*z[i]
		w_new = w_old - n*sum

		#if abs(cost(inner(w_new,z),y)-cost(inner(w_old,z),y))<err :
		#	break
		w_old = w_new
	return w_new

# Finding theta using an explicit solution
def regExplicit(z,y):
	z = np.asarray(z)
	w = np.dot(np.dot(np.linalg.inv(np.dot(z.T,z)),z.T),y)
	return w

# Finding alphas using dual solution
def regDual(z,y):
	#z = np.delete(z,(0), axis=1)
	z = np.asarray(z)

	G=np.empty([z.shape[0], z.shape[0]])
	for i in range (0,z.shape[0]):
		for j in range (i, z.shape[0]):
			G[i][j] = gauss(z[i],z[j],0.001)
			G[j][i] = G[i][j]
	a = np.dot(np.linalg.inv(G),y)
	return a

# Predicting the output value of x using primary solution
def predictPrimary(w,x):
	return inner(w,x)

# Predicting the output value of x using dual solution
def predictDual(a,x):
	yPred = np.empty([len(x)])
	for j in range(0,len(x)):
		y_hat=0
		for i in range(0,len(x)):
			y_hat = y_hat + a[i]*gauss(x[j],x[i],0.001)
		yPred[j] = y_hat
	return yPred

# Calculating cost function
def cost(yPred,y):
	n=len(y)
	err = 0
	for i in range(0,n):
		err = err + (y[i] - yPred[i])**2
	return err/2

# Mean squared error 
def mse(yPred,y):
	n=len(y)
	err = 0
	for i in range(0,n):
		err = err + (y[i] - yPred[i])**2
	return err/n

# Concatenation of two lists
def myConcat(x,l):
	outp=[]
	for i in range(0,len(x)):
		temp=[]
		for j in range(0,len(x[i])):
			temp.append(x[i][j])

		for j in range(0,len(l[i])):
			temp.append(l[i][j])
		outp.append(temp)
	outp=np.asarray(outp)
	return outp

# Adding several degrees of the single variable dataset to the data in order to fit polynomial model
def poly(x,n):
	l=[]
	for i in x:
		temp=[]
		for p in range(2,n+1):
			temp.append(np.power(i,p))
		l.append(temp)
	x=myConcat(x,l)
	return x

# Adding 2nd degree features to the dataset
def combFeatures_2(x):
	l=[]
	for i in x:
		temp=[]
		for j in range(0,len(i)):
			temp.append(i[j]*i[j])

			#full set
			#for k in range(j,len(i)):
			#	temp.append(i[j]*i[k])
		l.append(temp)

	x=myConcat(x,l)
	return x

# Adding 2nd & 3rd degree features to the dataset
def combFeatures_3(x):
	l=[]
	for i in x:
		temp=[]
		for j in range(0,len(i)):
			for k in range(j,len(i)):
				for k1 in range(k,len(i)):
					temp.append(i[j]*i[k]*i[k1])
		l.append(temp)

	#x=combFeatures_2(x)
	x=myConcat(x,l)
	return x

# Plot of the fitted model to the data
def plot(x,y,w):
	x = np.array(x)
	plt.plot(x[:,1], y, '.')
	plt.plot(x[:,1], predictPrimary(w,x), '.')
	plt.suptitle('Linear Model fitted to the Data')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()

# Scatter plot of the data
def plot_scatter(x,y):
	plt.scatter(x, y)
	plt.suptitle('Single feature 4')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()

def synthetic(n,m):
	x = np.random.rand(n,m)
	y = np.random.rand(n,1)
	rows = n
	return x,y,rows

# Cross Validation
def compute(z,y,rows):
	n_folds=10
	kf = KFold(rows, n_folds)
	avgErrorTraining=0;
	avgErrorTesting=0;

	for train, test in kf:
		xTrain=[]
		yTrain=[]
		xTest=[]
		yTest=[]
		tmp=[]

		for indx in train:
			xTrain.append(z[indx])
			yTrain.append(y[indx])
		for indy in test:
			xTest.append(z[indy])
			yTest.append(y[indy])

		w = regExplicit(xTrain,yTrain)
		#w = regIterative(xTrain,yTrain,0.00001,1)
		#w = regDual(xTrain,yTrain)
		#print w

		avgErrorTraining = avgErrorTraining + mse(predictPrimary(w,xTrain),yTrain)
		avgErrorTesting = avgErrorTesting + mse(predictPrimary(w,xTest),yTest)
		#avgErrorTraining = avgErrorTraining + mse(predictDual(w,xTrain),yTrain)
		#avgErrorTesting = avgErrorTesting + mse(predictDual(w,xTest),yTest)

		# Removing the column of 1s for the python built-in regression function
		xTrain = np.delete(xTrain,(0), axis=1)
		xTest = np.delete(xTest,(0), axis=1)
		regr = linear_model.LinearRegression()
		regr.fit(xTrain, yTrain)
		#print('Intercept, and Coefficients: \n', regr.intercept_, regr.coef_)
		#print("Testing error by python: %.2f" % mse(regr.predict(xTrain),yTrain))
		#print("Training error by python: %.2f" % mse(regr.predict(xTest),yTest))




############################################################################################## Main 
#x,y,rows=readFile("svar-set1.dat.txt")
#plot_scatter(x,y)

#x,y,rows = synthetic(20,20)
#x = x[0:50,:] #For reduction of training samples
#rows = 50

#x = poly(x,1) #For adding different degrees of features to the feature set for the single variable dataset
#x = combFeatures_2(x) #For adding combinational features to the feature set for the multivariate dataset
#x = np.vstack((np.ones(len(x)), x.T)).T #Adding ones to the first column of the dataset / This should be commented for the dual problem
#compute(x,y,rows) #Computing average training and testing error obtained with cross validation


out = open('largeOut', 'w')
with open("A-large.in", "r") as f:
		
		T = int(f.readline().strip())

		for i in range(T):
			a=set()
			N = f.readline().strip()
			out.write("Case #" + str(i+1) + ": ")

			b="INSOMNIA"
			for i in range(1000):
				tmp = (i+1)*int(N)
				for dig in str(tmp):
					a.add(dig)

				if (len(a)==10):
					b=tmp
					break

			#print (b)
			out.write(str(b) + "\n")

			#out.write("Case #" + str(i+1) + ": " + str(ind1) + " " + str(ind2) + "\n")

