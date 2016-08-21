#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import itertools
N = 32
J = 500
factor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def count_1s(n):
	cnt = 0
	while n > 0:
		if n % 2 == 1:
			cnt = cnt + 1
		n = n / 10
	return cnt

def to_base(n, base):
	ret = 0
	p = 0
	while n > 0:
		ret = ret + (base**p) * (n % 2)
		n = n / 10
		p = p + 1
	return ret

def find_factor(n):
	sq = int(math.sqrt(n)) + 1
	if n % 2 == 0:
		return 2
	i = 3
	retry = 0
	while i <= sq:
		if n % i == 0:
			return i
		i = i + 2
		retry = retry + 1
		if retry > 10000:
			return -1
	return -1
	
def solve(n):
	for d in range(2, 11):
		if d % 2 == 1:
			factor[d] = 2
			continue
		v = to_base(n, d)
		factor[d] = find_factor(v)
		if factor[d] == -1:
			return -1
	print n,
	for j in range(2, 11):
		print factor[j],
	print ""
	return 1
	
if __name__ == '__main__':
	beg = (1 << (N - 1))
	end = (1 << (N))
	while beg < end:
		beg = beg + 1
		to_dec = int("{0:b}".format(beg))
		if to_dec % 2 == 0:
			continue;
		if count_1s(to_dec) % 2 == 1:
			continue;
		if solve(to_dec) > 0:
			J = J - 1
		if J == 0:
			break;
		
