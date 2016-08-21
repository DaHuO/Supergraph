#!/usr/bin/env python
import sys

names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
D = {}


def process(S):
	rlt = []
	for c in S :
		if c in D:
			D[c] += 1
		else:
			D[c] = 1

	if 'Z' in D:
		for i in range(D['Z']):
			rlt.append(0)
			for c in names[0]:
				D[c] -= 1
	if 'W' in D:
		for i in range(D['W']):
			rlt.append(2)
			for c in names[2]:
				D[c] -= 1
	if 'X' in D:
		for i in range(D['X']):
			rlt.append(6)
			for c in names[6]:
				D[c] -= 1
	if 'G' in D:
		for i in range(D['G']):
			rlt.append(8)
			for c in names[8]:
				D[c] -= 1
	if 'H' in D:
		for i in range(D['H']):
			rlt.append(3)
			for c in names[3]:
				D[c] -= 1
	if 'R' in D:
		for i in range(D['R']):
			rlt.append(4)
			for c in names[4]:
				D[c] -= 1
	if 'F' in D:
		for i in range(D['F']):
			rlt.append(5)
			for c in names[5]:
				D[c] -= 1
	if 'V' in D:
		for i in range(D['V']):
			rlt.append(7)
			for c in names[7]:
				D[c] -= 1
	if 'I' in D:
		for i in range(D['I']):
			rlt.append(9)
			for c in names[9]:
				D[c] -= 1
	if 'E' in D:
		for i in range(D['E']):
			rlt.append(1)
	rlt.sort()
	s = ''
	for i in rlt:
		s += str(i)
	return s

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())	
for i in range(T):
	D = {}
	S = input_file.readline().strip()
	print 'Case #%d: ' % (i + 1), process(S)