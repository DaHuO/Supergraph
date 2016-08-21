#!/usr/bin/env python

from sys import stdin,stderr
from math import *

def cin():
	return stdin.readline()

def cinspi():
	return [int(s) for s in cin().split(' ')]

value = 1234

def getC(x, y):
	assert(x < r and y < c)
	tmp = x * c + y
	return (value >> tmp & 1) == 1

def coord(v):
	if (v <= c):
		return (-1, v - 1)
	if (v > c and v <= r + c):
		return (v - c - 1, c)
	if (v > r + c and v <= 2*c + r):
		return (r, 2 * c + r - v)
	if (v > 2 * c + r and v <= 2 * (r + c)):
		return (2 * (r + c) - v, -1)

def coordNext(v):
	if (v <= c):
		return (0, v - 1)
	if (v > c and v <= r + c):
		return (v - c - 1, c - 1)
	if (v > r + c and v <= 2*c + r):
		return (r - 1, 2 * c + r - v)
	if (v > 2 * c + r and v <= 2 * (r + c)):
		return (2 * (r + c) - v, 0)

def move(c0, c1):
	c = getC(c1[0], c1[1])
	if (c0[0] > c1[0]):
		return (0, 1) if c else (0, -1)
	elif (c0[0] < c1[0]):
		return (0, -1) if c else (0, 1)
	else:
		if (c0[1] < c1[1]):
			return (-1, 0) if c else (1, 0)
		elif (c0[1] > c1[1]):
			return (1, 0) if c else (-1, 0)
	assert(False)

def isValid(lover):
	v0,v1 = lover
	c0 = coord(v0)
	c01 = coordNext(v0)
	while (c01[0] >= 0 and c01[0] < r and c01[1] >= 0 and c01[1] < c):
		mov = move(c0, c01)
		c02 = (c01[0] + mov[0], c01[1] + mov[1])
		c01, c0 = c02, c01
	if (c01 == coord(v1)):
		return True
	if (value == 3):
		print >> stderr, v0, v1, c01
	return False

def check():
	for lover in lovers:
		if (not isValid(lover)):
			return False
	return True

testcase = int(cin())
for case in range(1, testcase + 1):
	print >> stderr, 'Running {} >>>>>>>>>>'.format(case)
	[r,c] = cinspi()
	lovers = []
	rlovers = cinspi()
	for j in range(r + c):
		lovers.append((rlovers[j * 2], rlovers[j * 2 + 1]))
		l = lovers[-1]
		print >> stderr, l[0], coord(l[0]), coordNext(l[0])
		print >> stderr, l[1], coord(l[1]), coordNext(l[1])

	output = [[False] * c for i in range(r)]
	possible = True

	for i in range(0, 2 ** (r * c)):
		value = i
		if (check()):
			break
		value = None

	if (value is None):
		print 'Case #{}: \n{}'.format(case, 'IMPOSSIBLE')
	else:
		print 'Case #{}: '.format(case)
		for ri in range(r):
			s = []
			for ci in range(c):
				s.append('/' if getC(ri, ci) else '\\')
			print ''.join(str(v) for v in s)

	print >> stderr, 'Case {} Finished >>>>>>>>>>'.format(case)
	assert(True)
