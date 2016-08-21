#!/usr/bin/env python3
import sys

def solve(N):
	if not N: return "INSOMNIA"
	digits = set()
	c = 1
	
	while True:
		d = "%s" % (c*N)
		for i in d:
			digits.add(i)
		if(len(digits) == 10):
			return "%s" % (c*N)
		c += 1

	return ""

cases = int(sys.stdin.readline())

for case in range(cases):
	N = int(sys.stdin.readline()[:-1])
	print ("Case #%d: %s" % (case+1,solve(N)))
