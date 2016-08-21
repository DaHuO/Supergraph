#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		N, K = map(int, raw_input().split())
		probs = map(float, raw_input().split())
		assert len(probs) == N
		yield (N, K, probs)
	return


def writeOutput(results):
	for result in results:
		print result
	return
## I/O functions begin
#######################


def prob_of_k_yeses(probs, k):
	if k > len(probs):
		return float(0)
	if len(probs) == 0:
		if k == 0:
			return float(1)
		return float(0)
	p = probs[0]
	return p * prob_of_k_yeses(probs[1:], k-1) + (float(1)-p) * prob_of_k_yeses(probs[1:], k)

def fill_out_dp_dict(probs, k):
	dp = {}
	# (last_j, k) -> prob in [0,1]
	dp[(0, 0)] = 1.0
	for curr_k in range(1, k):
		dp[(0, curr_k)] = 0.0
		
	for j in range(1, len(probs) + 1):
		for curr_k in range(k):
			if curr_k > j:
				dp[(j, curr_k)] = 0
			elif curr_k == 0:
				prob = reduce(lambda a, b: a*b, map(lambda x: 1.0 - x, probs[-1 * j:]))
				dp[(j, curr_k)] = prob
			else:
				p = probs[-1 * j]
				dp[(j, curr_k)] = p * dp[(j-1, curr_k - 1)] + (1.0 - p)*dp[(j-1, curr_k)]
	return dp[(len(probs), k / 2)]



def ALGORITHM(test_case):
	N, K, probs = test_case
	import itertools
	best = 0.0
	for l in list(itertools.combinations(probs, K)):
		p = fill_out_dp_dict(l, K)
		if p > best:
			best = p
	return str(best)

	
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
