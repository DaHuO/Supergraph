#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		N, R, P, S = map(int, raw_input().split())
		assert R + P + S == 2**N
		yield (N, R, P, S)
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################


def ALGORITHM(test_case):
	N, R, P, S = test_case
	if N <= 3:
		return BRUTE_FORCE(test_case)

def winner(a, b):
	lo, hi = min(a,b), max(a,b)
	if lo == "P":
		if hi == "R":
			return "P"
		elif hi == "S":
			return "S"
		raise ValueError("tie")
	elif lo == "R":
		if hi == "S":
			return "R"
		raise ValueError("tie")
	raise ValueError("tie")

def tourny_concludes(S):
	if len(S) == 1:
		return True
	next_S = ""
	for i in range(len(S) / 2):
		if S[2*i] == S[2*i + 1]:
			return False
		next_S = next_S + winner(S[2*i], S[2*i + 1])
	return tourny_concludes(next_S)


	
def BRUTE_FORCE(test_case):
	N, R, P, S = test_case
	S = "P"*P + "R"*R + "S"*S
	from itertools import permutations
	perms = [''.join(p) for p in permutations(S)]
	perms = sorted(perms)
	for s in perms:
		if tourny_concludes(s):
			return s
	return "IMPOSSIBLE"


def basic_test():
	assert tourny_concludes("PR") == True
	assert tourny_concludes("PSRS") == True
	assert tourny_concludes("RR") == False

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
