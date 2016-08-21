#!/usr/bin/env python3

import sys

def in_base(n, b):
	r = 0
	m = 1
	while n:
		r += m * (n % 2)
		n //= 2
		m *= b
	return r

# some sanity checks for in_base
for i in [23, 42, 1337, 9001]:
	ib = bin(i)[2:]
	for b in range(2,11):
		assert in_base(i, b) == int(ib, b)

T, N, J = map(int, sys.stdin.read().split())
assert T == 1

print('Case #1:')

x = (1<<(N-1)) | 1
while J:
	divisors = []

	for b in range(2,11):
		xb = in_base(x, b)
		for d in range(2, min(xb, 100000)):
			if xb % d == 0:
				divisors.append(d)
				break
		else:
			break

	if len(divisors) == 9:
		print(bin(x)[2:], *divisors)
		J -= 1
	x += 2
