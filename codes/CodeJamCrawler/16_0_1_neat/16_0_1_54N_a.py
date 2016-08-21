#!/usr/bin/python

import sys

data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

def solve(x):
	assert isinstance(x, (int,long))
	seen = {}
	r = 0
	for i in range(1,100):
		xs = str(x*i)
		for xn in xs:
			seen[xn] = True
		if len(seen) == 10:
			r = long(xs)
			break
	return r

case = 1
while len(data_lines):
	x = int(data_lines.pop())
	r = solve(x)
	print 'Case #%d: %s' % (case, str(r) if r > 0 else "INSOMNIA")
	case += 1
