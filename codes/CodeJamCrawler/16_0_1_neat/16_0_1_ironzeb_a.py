from __future__ import print_function

import sys

f = sys.stdin
T = int(f.readline())

def digits_in(N):
	digits = str(N)
	return set(int(c) for c in digits)

def solve(N):
	if N == 0:
		return "INSOMNIA"

	digits = set()
	for n in range(N, N*100, N):
		digits |= digits_in(n)
		if len(digits) == 10:
			return n
	return "INSOMNIA"

for t in range(1, T+1):
	N = int(f.readline())
	ans = solve(N)
	print("Case #{}: {}".format(t, ans))

