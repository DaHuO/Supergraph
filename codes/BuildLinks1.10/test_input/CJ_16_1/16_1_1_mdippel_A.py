#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		S = str(raw_input())
		yield S
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################

def brute_force(curr, remain):
	if len(remain) == 0:
		yield curr
	else:
		for output in brute_force(curr + remain[0], remain[1:]):
			yield output
		for output in brute_force(remain[0] + curr, remain[1:]):
			yield output


def ALGORITHM(test_case):
	S = test_case
	best = S
	for S in brute_force("", S):
		if S > best:
			best = S
	return best 
	
def basic_test():
	pass

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
