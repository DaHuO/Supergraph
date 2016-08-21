#!/usr/bin/env python

import sys

with open(sys.argv[1]) as input:
	input.next()
	for case, line in enumerate(input, 1):
		N = int(line.strip())
		if not N:
			print 'Case #%s: INSOMNIA' % case
			continue
		seen = set()
		current = 0
		while len(seen) < 10:
			current += N
			seen.update(str(current))
		print 'Case #%s: %s' % (case, current)