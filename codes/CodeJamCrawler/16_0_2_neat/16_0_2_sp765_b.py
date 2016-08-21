#!/usr/bin/python

import sys
import math

def equal(a,b):
	return math.rabs(a-b) <= 0.000001

def solve(S):
	last = '.'
	numSeg = 0
	for c in S:
		if c != last:
			numSeg += 1
		#print c, numSeg
		last = c

	if S[-1] == '+':
		numSeg -= 1

	return numSeg

if __name__ == "__main__":
	T = int(sys.stdin.readline())

	for t in range(T):
		S = sys.stdin.readline().strip()
		print "Case #{}: {}".format(t+1, solve(S))
