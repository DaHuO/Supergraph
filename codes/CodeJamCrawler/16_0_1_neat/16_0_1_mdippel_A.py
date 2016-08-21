#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		N = int(raw_input())
		yield N
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################


def ALGORITHM(test_case):
	N = test_case
	seen = [False] * 10
	curr = N
	if curr == 0:
		return "INSOMNIA"
	while True:
		for c in str(curr):
			seen[int(c)] = True
		done = reduce(lambda a,b: a and b, seen)
		#print sum(seen)
		if done:
			return str(curr)
		curr = curr + N
	
def basic_test():
	assert(ALGORITHM(0) == "INSOMNIA")
	assert(ALGORITHM(1) == "10")
	assert(ALGORITHM(2) == "90")
	assert(ALGORITHM(11) == "110")
	assert(ALGORITHM(1692) == "5076")

def runAlgorithm():
	results = []
	for test_case in processInput():
		results.append(ALGORITHM(test_case))

	for i in range(len(results)):
		results[i] = "Case #" + str(i+1) + ": " + results[i] + "\n"

	writeOutput(results)

if __name__ == "__main__":
	basic_test()
	#while True:
	#	for i in range(1, 10**6):
	#		print i, ALGORITHM(i)
	runAlgorithm()
