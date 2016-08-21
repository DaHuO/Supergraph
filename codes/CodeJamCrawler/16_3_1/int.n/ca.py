#!/usr/bin/env python
import sys
import itertools

names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
parties = []

def process(total):
	global parties
	rlt = ''
	while total > 0:
		parties.sort()
		p = parties[-1][1]
		parties[-1][0] -= 1
		total -= 1
		if parties[-2][0] > total / 2:
			p += parties[-2][1]
			parties[-2][0] -= 1
			total -= 1
		rlt += p + ' '
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	N = int(input_file.readline())
	nums = map(int, input_file.readline().split())
	parties = []
	total = 0
	for j in range(N):
		parties.append([nums[j], names[j]])
		total += nums[j]
	print 'Case #%d:' % (i + 1), process(total)