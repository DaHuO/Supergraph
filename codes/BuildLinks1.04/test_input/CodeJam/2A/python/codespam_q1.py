#!/usr/bin/env python

import re
import sys

def e(s):
	r = ''
	for c in s:
		if c == 'R':
			r += 'RS'
		elif c == 'S':
			r += 'PS'
		else:
			assert c == 'P'
			r += 'PR'
	return r


def run(N, C):
	for w in 'RPS':
		r = 0
		s = w

		for r in range(1, N + 1):
			s = e(s)
			if r % 2 != N % 2:
				s = s[::-1]

		if all(len(re.findall(c, s)) == C[c] for c in 'RPS'):
			return s

	return 'IMPOSSIBLE'


for i, l in enumerate(sys.stdin.read().splitlines()[1:]):
	N, R, P, S = map(int, l.split())
	C = {'R': R, 'P': P, 'S': S}
	print 'Case #%d: %s' % (i + 1, run(N, C))
