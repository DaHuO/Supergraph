#!/usr/bin/python

import sys
from sets import Set

lineNum = 0
for line in sys.stdin:
	lineNum += 1
	if lineNum == 1:
		continue
	n = int(line)
	res = ''
	seenDigits = Set()
	if n == 0:
		res = 'INSOMNIA'
	counter = 1
	while res == '':	
		nStr = str(counter * n)
		for c in nStr:
			if c not in seenDigits:
				seenDigits.add(c)
			if len(seenDigits) == 10:
				res = nStr
				break
		counter += 1
	print 'Case #{0}: {1}'.format(lineNum - 1, res)
