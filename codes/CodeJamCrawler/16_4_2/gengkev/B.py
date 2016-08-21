#!/usr/bin/env python3

import itertools
import sys

def calcProb(c, comb):
	#print('begin', comb)
	counts = [0.0 for _ in range(c+1)]
	counts[0] = 1.0

	for prob in comb:
		nextCounts = [0.0 for _ in range(c+1)]
		aux = [0 for _ in range(c+1)]
		for j in range(c+1):
			nextCounts[j] += counts[j] * prob
			aux[j] += 1
			if j < c:
				nextCounts[j+1] += counts[j] * (1 - prob)
				aux[j+1] += 1
		#for j in range(c+1):
		#	nextCounts[j] /= aux[j]

		#print(nextCounts, aux)
		counts = nextCounts

	return counts[c]


def solve(n, k, arr):
	bestProb = 0.0
	for comb in itertools.combinations(range(n), k):
		nums = [arr[i] for i in comb]
		prob = calcProb(k//2, nums)
		if prob > bestProb:
			bestProb = prob
	return bestProb


N = int(input())
for t in range(1, N+1):
	n, k = map(int, input().split())
	arr = list(map(float, input().split()))
	ans = solve(n, k, arr)
	print('Case #%d: %.8f' % (t, ans)) 
	print(t, file=sys.stderr)

