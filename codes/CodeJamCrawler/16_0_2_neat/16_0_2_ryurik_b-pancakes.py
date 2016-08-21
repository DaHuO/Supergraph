#!/usr/bin/python3

import sys

def flip(s, n):
	s = list(s)
	s1 = s[:n]
	s2 = s[n:]
	s1.reverse()
	s1 = ['-' if x == '+' else '+' for x in s1]
	return ''.join(s1 + s2)

def solve(s):
	pending = [(s, 0)]
	visited = set()
	while len(pending) > 0:
		v, c = pending.pop(0)
		if set(v) == set('+'):
			return c
		visited.add(v)
		for i in range(len(s)):
			nv = flip(v, i + 1)
			if nv not in visited:
				pending.append((nv, c + 1))

if __name__ == '__main__':
	T = int(sys.stdin.readline())

	for t in range(1, T + 1):
		S = sys.stdin.readline().strip()
		print('Case #%d: %s' % (t, solve(S)))
