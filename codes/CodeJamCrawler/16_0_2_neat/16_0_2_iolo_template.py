#!/usr/bin/python

import sys

def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***
	case = case.strip() + "+"
	res=0
	for p in xrange(len(case)-1):
		if case[p]!=case[p+1]:
			res+=1
	return str(res)

	# *** END CODE PROCESSING CASE ***
	return 

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
		
	# *** END CODE READING CASE ***

	solution=processCase(caseInput)
	print "Case #"+str(case)+": "+solution

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

