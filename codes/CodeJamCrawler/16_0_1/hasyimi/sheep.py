#!/usr/bin/env python

from sys import stdin

def last_sheep(p):
	if p == 0:
		return None

	d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	i = 0
	while len(d) > 0:
		i = i + 1
		q = p * i
		while q != 0:
			di = q % 10
			if di in d:
				d.remove(di)
			if len(d) == 0:
				break
			q = q / 10

	return p * i

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	p = long(stdin.readline().rstrip('\n'))
	l = last_sheep(p)
	print "Case #%d: %s" % (i + 1, str(l) if l else "INSOMNIA")
