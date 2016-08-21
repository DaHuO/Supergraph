#!/usr/bin/python

import sys
import math

def equal(a,b):
	return math.rabs(a-b) <= 0.000001

def interpret(N, coin, d):
	val = 0
	base = 1
	for i in range(N):
		if (1 << i) & coin != 0:
			val += base
		base *= d
	return val

def find_factor(val):
	for i in range(2, int(math.sqrt(val))+1):
		if val % i == 0:
			return i
	return -1

def solve(N, J):
	found = 0
	i = 1
	while found < J:
		coin = i + (1 << (N-1))
		jam = True
		factors = []
		for d in range(2, 11):
			val = interpret(N, coin, d)
			factor = find_factor(val)
			if factor == -1:
				jam = False
				break
			factors.append(str(factor))

		#print coin
		if jam:
			print "{} {}".format(bin(coin)[2:], ' '.join(factors))
			found += 1
		i += 2

if __name__ == "__main__":
	T = int(sys.stdin.readline())
	#print T
	for t in range(T):
		#print sys.stdin.readline().split()
		N, J = map(int, sys.stdin.readline().split())
		print "Case #{}:".format(t+1)
		solve(N, J)