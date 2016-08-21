#!/usr/local/bin/python3

from sys import stdin,stdout,stderr,exit
from math import ceil

ncases = int(stdin.readline())

for case in range(1, ncases + 1):
	line = stdin.readline().split()
	
	K = int(line[0])
	C = int(line[1])
	S = int(line[2])

	s = ceil(K/C)
	if S < s:
		stdout.write('Case #%u: IMPOSSIBLE\n' % case)
	else:
		stdout.write('Case #%u:' % case)
		for i in range(0, s):
			loc = 0
			for j in range(0, C):
				coord = i*C+j
				if coord >= K:
					coord = K-1
				loc = loc + coord*(K**(C-j-1))
			stdout.write(' %u' % (loc + 1))

		stdout.write('\n')