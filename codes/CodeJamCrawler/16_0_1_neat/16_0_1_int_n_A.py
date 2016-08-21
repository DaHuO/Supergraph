#!/usr/bin/env python
import sys
import itertools

digits = []

def isDone():
	for i in digits:
		if not i:
			return False
	return True

def mark(n):
	while n > 0:
		m = n % 10
		digits[m] = True
		n /= 10

def process(N):
	if N == 0:
		return 'INSOMNIA'
	M = N
	while True:
		mark(M)
		if isDone():
			return M
		M += N

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	digits = [False] * 10
	N = int(input_file.readline())
	print 'Case #%d:' % (i + 1), process(N)
