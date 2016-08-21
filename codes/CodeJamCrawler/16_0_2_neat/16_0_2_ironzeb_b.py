from __future__ import print_function

import sys

f = sys.stdin
T = int(f.readline())

def solve(s):
	if len(s) == 0:
		return 0

	last_minus = s.rfind("-")
	if last_minus == -1:
		return 0

	s = s[:last_minus]

	d = {"-": "+", "+": "-"}
	s = ''.join(d[c] if c in d else c for c in s)
	return 1 + solve(s)

for t in range(1, T+1):
	s = f.readline().strip()
	ans = solve(s)
	print("Case #{}: {}".format(t, ans))

