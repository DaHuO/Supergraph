#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		s = str(raw_input())
		yield s
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################

def min_happy(s):
	if len(s) == 0:
		return 0
	if s[-1] == "+":
		return min_happy(s[:-1])
	else:
		return 1 + min_unhappy(s[:-1])

def min_unhappy(s):
	if len(s) == 0:
		return 0
	if s[-1] == "-":
		return min_unhappy(s[:-1])
	else:
		return 1 + min_happy(s[:-1])



def ALGORITHM(test_case):
	s = test_case
	return str(min_happy(s))

	
def basic_test():
	assert(ALGORITHM("-") == "1")
	assert(ALGORITHM("-+") == "1")
	assert(ALGORITHM("+-") == "2")
	assert(ALGORITHM("+++") == "0")
	assert(ALGORITHM("--+-") == "3")

def runAlgorithm():
	results = []
	for test_case in processInput():
		results.append(ALGORITHM(test_case))

	for i in range(len(results)):
		results[i] = "Case #" + str(i+1) + ": " + results[i] + "\n"

	writeOutput(results)

if __name__ == "__main__":
	basic_test()
	runAlgorithm()
