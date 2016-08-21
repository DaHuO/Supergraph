#!/usr/bin/env python
#
# Lars Lindgren <chrono@eeky.net>
#
import sys

def count_sheep(n):
	if n == 0:
		return 'INSOMNIA'
	count = 1
	seen = set()
	while True:
		d = n * count
		seen = seen.union(set(map(int, str(d))))
		if len(seen) == 10:
			return d
		count += 1

filename = sys.argv[1]
fin = open(filename, 'r')
cases = int(fin.readline())
for c in xrange(1, cases + 1):
	n = int(fin.readline())
	print 'Case #%d: %s' % (c, count_sheep(n))
