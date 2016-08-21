#!/usr/bin/env python
import sys

lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == len(lines)-1)


def gold_positions(K, C, S):
	assert(K >= 1 and K <= 100)
	assert(C >= 1 and C <= 100)
	if S < K:
		return "IMPOSSIBLE"
	else:
		return " ".join([str(i) for i in range(1, K+1)])

for i in range(1, T+1):

	K, C, S = [int(v) for v in lines[i].split()]

	result = range(2, S) if S >= (K - 1) else "IMPOSSIBLE"
	sys.stdout.write("Case #{}: {}\n".format(i, gold_positions(K, C, S)))
