#!/usr/bin/env python

from sys import stdin
from operator import itemgetter

def contigs(p):
	chunks = []
	s = p[0]
	i = 1
	ck = [s, 0, 1]
	while i < len(p):
		if p[i] == s:
			ck[0] += s
			ck[2] += 1
		else:
			chunks.append(ck)
			s = p[i]
			ck = [s, i, 1]
		i += 1
	chunks.append(ck)

	chunks = sorted(chunks, key=itemgetter(2), reverse=True)
	return map(lambda x:x[1], chunks)

def flip(p, n):
	return p[:n].replace('+', 'x').replace('-', '+').replace('x', '-') + p[n:]

def flip_count(p):
	if p == '+' * len(p):
		return 0
	if p == '-' * len(p):
		return 1

	n = 0
	while p != '+' * len(p):
		ct = contigs(p)
		if p == '-' * len(p):
			p = flip(p, len(p))
			n += 1

		for c in ct:
			if p[0] != p[c]:
				p = flip(p, c)
				n += 1
				break

	return n

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	p = stdin.readline().rstrip('\n')
	print "Case #%d: %s" % (i + 1, flip_count(p))
