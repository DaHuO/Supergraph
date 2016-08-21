#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		K, C, S = map(int, raw_input().split())
		yield (K, C, S)
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################


def ALGORITHM(test_case):
	K, C, S = test_case
	# K - length of original artwork
	# C - number of layers. C=1 is the original artwork
	# S - number of graduate students available
	if C == 1 and S == K:
		return " ".join(map(str, range(1, S+1)))
	elif C == 1 and S < K:
		return "IMPOSSIBLE"
	elif S == K:
		choices = []
		x = 1
		for i in range(K):
			choices.append(x + i*K**(C-1))
		return " ".join(map(str, choices))
	
def basic_test():
	#assert(ALGORITHM((2,3,2)) == "2"), ALGORITHM((2,3,2))
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
