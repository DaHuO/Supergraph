# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 23:09:21 2016

@author: dan
"""


def solve(x):#input
	n=0
	last=''
	for i in x:
		if last=='':
			if i=='-':
				n=n+1
		else:
			if last=='+':
				if i=='-':
					n=n+2
		last=i
	return n

test=[]
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	test.append(raw_input().strip())



for i in range(1,t+1):
	print "Case #"+str(i)+": "+str(solve(test[i-1]))
