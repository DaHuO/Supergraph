#!/usr/bin/env python3
import sys

def solve(w):


	out = w[0]
	
	for x in range(1,len(w)):
		c = w[x]
		if c < out[0]:
			out += c
		else:
			out = c + out
	return out

cases = int(sys.stdin.readline())

for case in range(cases):
	w = sys.stdin.readline()[:-1]
	print("Case #%d: %s" % (case+1,solve(w)))
		