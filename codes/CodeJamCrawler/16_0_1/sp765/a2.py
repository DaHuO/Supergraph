#!/usr/bin/python

import sys
import math

def equal(a,b):
	return math.rabs(a-b) <= 0.000001

def solve(S):
	T = ''
	for c in S:
		if T + c > c + T:
			T = T + c
		else:
			T = c + T
	return T


if __name__ == "__main__":
	T = int(sys.stdin.readline())

	for t in range(T):
		S = sys.stdin.readline().strip()
		print "Case #{}: {}".format(t+1, solve(S))

