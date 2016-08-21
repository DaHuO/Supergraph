#!/usr/bin/env python3
import sys

def solve(p):
	g = 1
	i = p[0]
	for x in p:
		if x != i:
			g += 1
			i = x
	if p[-1] == '+':
		g -= 1
	return g

cases = int(sys.stdin.readline())

for case in range(cases):
	p = sys.stdin.readline()[:-1]
	print("Case #%d: %d" % (case+1,solve(p)))
