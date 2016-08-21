#!/usr/bin/env python
import sys

hl = []
N = 0

def process():
	rlt = ''
	rl = []
	for i in range(2501):
		if hl[i] % 2 <> 0:
			rl.append(i)
	rl.sort()
	for i in rl:
		rlt += ' ' + str(i)
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	hl = [0] * 2501
	N = int(input_file.readline())
	for j in range(2 * N - 1):
		l = map(int, input_file.readline().split())
		for h in l:
			hl[h] += 1
	print 'Case #%d:' % (i + 1), process()