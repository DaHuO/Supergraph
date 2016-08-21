#!/bin/python

import sys

def removeThings(num, x, list):
	for ch in str(num*x):
		list = filter(lambda x: x is not int(ch), list)
	return list

def doThing(x):
	if x is 0:
		return "INSOMNIA"
	numList = [0,1,2,3,4,5,6,7,8,9]
	i = 0
	while numList:
		i += 1 
		numList = removeThings(i, x, numList)
	return i*x

n = int(raw_input().strip())
for row in xrange(n):
	print "Case #" + str(row+1) + ": " + str(doThing(int(raw_input().strip())))