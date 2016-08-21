#!/usr/bin/python

import sys
import numpy as np

if len(sys.argv) != 2:
	print "usage: ./b.py <input_file_name>"
	exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
	output_file_name = input_file_name[:-3] + ".out"
else:
	output_file_name = input_file_name + ".out"

def calcP(P):
	d = []
	tmp = {}
	for i in xrange(-len(P) - 2, len(P) + 2 + 1, 2):
		tmp[i] = 0.0
	tmp[0] = 1.0
	d.append(tmp)
	for i in xrange(len(P) / 2):
		p1, p2 = P[i * 2:i * 2 + 2]
		p_minus2 = (1 - p1) * (1 - p2)
		p_plus2 = p1 * p2
		p_tie = (1 - p1) * p2 + p1 * (1 - p2)
		tmp = {}
		for j in xrange(-len(P) - 2, len(P) + 2 + 1, 2):
			tmp[j] = 0.0
		for j in xrange(-i * 2 - 2, i * 2 + 2 + 1, 2):
			tmp[j] = d[i][j - 2] * p_plus2 + d[i][j] * p_tie + d[i][j + 2] * p_minus2
		d.append(tmp)
	neg = 0
	pos = 0
	for key in d[-1]:
		if key < 0:
			neg += d[-1][key]
		elif key > 0:
			pos += d[-1][key]
	return d[-1][0], neg, pos

def dfs(K, P, a):
	global ret, resultP
	if K == 0:
		tmp, neg, pos = calcP(a)
		if tmp > ret:
			ret = tmp
			resultP = a[:]
		return
	for i in xrange(len(P) - K + 1):
		p = P[i]
		a.append(p)
		dfs(K - 1, P[i + 1:], a)
		a.pop()

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		d = f.readline()
		N, K = [int(x) for x in d.split(' ')]
		d = f.readline()
		P = [float(x) for x in d.split(' ')]
		P.sort()
		ret = 0
		resultP = []
		for c2 in xrange(K + 1):
			c1 = K - c2
			arr = P[:c1] + P[len(P) - c2:]
			tmp, neg, pos = calcP(arr)
			if tmp > ret:
				ret = tmp
				resultP = arr[:]
		print P
		print sorted(resultP)
		print '------------------------'
		results.append(ret)

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
