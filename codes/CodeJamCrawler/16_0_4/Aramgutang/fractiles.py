#!/usr/bin/env python

import sys

with open(sys.argv[1]) as input:
	input.next()
	for case, line in enumerate(input, 1):
		K, C, S = map(int, line.strip().split(' '))
		if K <= S:
			answer = ' '.join(map(str, range(1, K+1)))
		else:
			if S < (K - 1 + C):
				answer = 'IMPOSSIBLE'
		print 'Case #%s: %s' % (case, answer)