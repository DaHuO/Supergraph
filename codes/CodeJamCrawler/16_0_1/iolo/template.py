#!/usr/bin/python

import sys

def processCase(case):
	# *** BEGIN CODE PROCESSING CASE ***

	N = int(case)
	if N==0:
		return "INSOMNIA"
	digits=set()
	it=1
	while True:
		Ns=str(N*it)
		for digit in Ns:
			digits.add(digit)
			if len(digits)==10:
				return Ns
		it += 1


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

