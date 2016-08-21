# coding: utf-8

import os, sys, re, string
import math,random

def solve(N, P):
	names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	p = map(lambda x: [x[0], x[1]], zip(names, P))
	count = reduce(lambda a,b: a + b, [0] + P)
	res = []
	while len(p) > 0:
		p.sort(lambda a, b: b[1] - a[1])
		if len(p) == 1:
			res.append(p[0][0])
			break
		elif count == 3:
			res.append(p[0][0])
			p = p[1:]
			count -= 1
		else:
			s = p[0][0]
			if p[0][1] >= p[1][1] + 1 and p[0][1] >= 2:
				s += s
				p[0][1] -= 2
			else:
				s += p[1][0]
				p[0][1] -= 1
				p[1][1] -= 1
			res.append(s)
			if p[0][1] == 0:
				p = p[1:]
			if p[0][1] == 0:
				p = p[1:]
			count -= 2
	return " ".join(res)

def main():
	T = int(sys.stdin.readline())
	for i in xrange(1, T + 1):
		N = int(sys.stdin.readline())
		P = map(int, sys.stdin.readline().split(' '))
		print "Case #%d: %s" % (i, solve(N, P))

if __name__ == '__main__':
	main()


