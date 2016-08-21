#!/usr/local/bin/python3

from sys import stdin,stdout,stderr,exit

ncases = int(stdin.readline())

for case in range(1, ncases + 1):
	N = int(stdin.readline().strip())

	if N == 0:
		stdout.write('Case #%u: INSOMNIA\n' % case)
		continue
	
	seen = set()
	for i in range(1,1000000):
		seen = seen.union(repr(i*N))
		if len(seen) == 10:
			break

	stdout.write('Case #%u: %u\n' % (case, i*N))
