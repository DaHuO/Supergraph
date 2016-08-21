#!/usr/bin/env python
import sys

MAX_ITERATIONS = 10*1000*1000

def find_sleep_number(N):
	if N == 0:
		return "INSOMNIA"
	digits = set()
	i = 0
	while len(digits) < 10:
		i += 1
		digits.update(str(N*i))
		if i > MAX_ITERATIONS:
			return "INSOMNIA"
	return N*i
	
lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == len(lines)-1)
for i in range(1, T+1):
	N = int(lines[i])
	sys.stdout.write("Case #{}: {}\n".format(i, find_sleep_number(N)))
