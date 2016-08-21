#!/usr/bin/python

import sys

def tilesToBeCleaned(K, C, S):	
	return ' '.join([str(i) for i in range(1, K + 1)])

lineNum = 0
for line in sys.stdin:
	lineNum += 1
	if lineNum == 1:
		continue
	K, C, S = [int(a) for a in line.split(' ')]
	print 'Case #{0}: {1}'.format(lineNum - 1, tilesToBeCleaned(K, C, S))
