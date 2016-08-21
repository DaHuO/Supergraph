#!/usr/bin/python

import sys
import math

def equal(a,b):
	return math.rabs(a-b) <= 0.000001

def solve(N):
	if N == 0:
		return "INSOMNIA"

	left = set(range(0,10))
	i = 0
	while left:
		i += 1
		num = i * N
		while num > 0:
			left.discard(num%10)
			num /= 10
	return i * N

if __name__ == "__main__":
	T = int(sys.stdin.readline())

	for t in range(T):
		N = int(sys.stdin.readline())
		print "Case #{}: {}".format(t+1, solve(N))
