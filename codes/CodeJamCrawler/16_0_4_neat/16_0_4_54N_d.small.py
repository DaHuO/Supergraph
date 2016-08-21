#!/usr/bin/python

import sys

data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

case = 1
while len(data_lines):
	K,C,S = [int(x) for x in data_lines.pop().split(' ')]
	print 'Case #%d: %s' % (case, " ".join([str(x) for x in xrange(1,K+1)]))
	case += 1
