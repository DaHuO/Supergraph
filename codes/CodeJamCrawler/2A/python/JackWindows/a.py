#!/usr/bin/python

import sys
import numpy as np

if len(sys.argv) != 2:
	print "usage: ./a.py <input_file_name>"
	exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
	output_file_name = input_file_name[:-3] + ".out"
else:
	output_file_name = input_file_name + ".out"

def solve(R, P, S):
	if R + P + S == 1:
		if R == 1:
			return 'R'
		elif P == 1:
			return 'P'
		elif S == 1:
			return 'S'
	a = P + R - S
	b = R + S - P
	c = P + S - R
	if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
		return 'IMPOSSIBLE'
	x = a / 2
	y = b / 2
	z = c / 2
	if x < 0 or y < 0 or z < 0:
		return 'IMPOSSIBLE'
	r = solve(R - x, P - z, S - y)
	if r == 'IMPOSSIBLE':
		return 'IMPOSSIBLE'
	ret = ''
	for c in r:
		if c == 'R':
			ret += 'RS'
		elif c == 'P':
			ret += 'PR'
		elif c == 'S':
			ret += 'PS'
	return ret

def sort_result(s):
	if s == 'IMPOSSIBLE':
		return s
	if len(s) == 1:
		return s
	a = s[:len(s) / 2]
	b = s[len(s) / 2:]
	x = sort_result(a)
	y = sort_result(b)
	if x < y:
		return x + y
	else:
		return y + x

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		line = f.readline()
		N, R, P, S = [int(x) for x in line.split(' ')]
		ret = solve(R, P, S)
		ret = sort_result(ret)
		results.append(ret)

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
