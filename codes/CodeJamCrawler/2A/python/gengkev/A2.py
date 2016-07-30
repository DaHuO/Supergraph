#!/usr/bin/env python3

import itertools

def makeStuff(n, i, trip):
	reverse = (n % 2 == 0)
	arr = ['PRS'[i]]
	for j in range(n):
		nextArr = []
		for el in arr:
			remaining = {'P', 'R', 'S'} - {el}
			nextArr.extend(sorted(remaining, reverse=reverse))
		arr = nextArr
		reverse = not reverse
	return arr


def getNums(n, s):
	counts = [0, 0, 0]
	counts[s] = 1
	for i in range(n):
		counts = [
			counts[1] + counts[2],
			counts[0] + counts[2],
			counts[0] + counts[1]
		]
	return counts


def solve(n, r, p, s):
	trip = [p, r, s]
	for i in range(3):
		if trip == getNums(n, i):
			return makeStuff(n, i, trip)
	return None



N = int(input())
for t in range(1, N + 1):
	n, r, p, s = map(int, input().split())
	perm = solve(n, r, p, s)
	print('Case #%d:' % t, ''.join(perm) if perm else 'IMPOSSIBLE')


