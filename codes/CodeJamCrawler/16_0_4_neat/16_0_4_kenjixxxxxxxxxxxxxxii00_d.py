#!/usr/bin/env python

import sys

def sol(start, finish):
	r = ""
	for i in range(start, finish):
		r += " " + str(i)
	return r

def f(k, c, s):
	if k == 1:
		return " 1"
	if c == 1:
		if s < k:
			return " IMPOSSIBLE"
		else:
			return sol(1, k+1)
	if s < k - 1:
		return " IMPOSSIBLE"
	else:
		return sol(2, k+1)

def main():
	N = int(raw_input())
	for i in range(N):
		(k, c, s) = raw_input().split()
		k = int(k)
		c = int(c)
		s = int(s)
		print "Case #" + str(i+1) + ": " + f(k, c, s)
		
if __name__ == '__main__':
	main()
