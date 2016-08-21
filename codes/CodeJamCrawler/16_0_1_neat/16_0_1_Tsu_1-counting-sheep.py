#!/usr/bin/python3

import os, sys

def solve(N):
	digits = [False] * 10
	i = N
	while True:
		divided = i
		while divided != 0:
			digits[divided % 10] = True
			divided //= 10
		if all(digits):
			return i
		i += N

T = int(input())
for case in range(1, T + 1):
	N = int(input())
	if N == 0:
		print("Case #{0}: INSOMNIA".format(case))
	else:
		print("Case #{0}: {1}".format(case, solve(N)))
