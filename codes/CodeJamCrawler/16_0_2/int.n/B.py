#!/usr/bin/env python
import sys
import itertools

def eval(c):
	if c == '+':
		return 1
	return 0

def process(s):
	pre = eval(s[0])
	cur = eval(s[0])
	rlt = 0
	for i in range(1, len(s)):
		cur = eval(s[i])
		if pre == cur:
			continue
		pre = cur
		rlt += 1
	if cur == 0:
		rlt += 1
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	stack = input_file.readline().strip()
	print 'Case #%d:' % (i + 1), process(stack)
