# Coin Jam

import fileinput
from math import sqrt
from itertools import product, count, islice

def divisor(n):
	if n == 1: return 1
	if n%2 == 0: return 2
	for i in range(3, int(sqrt(n) + 1), 2):
		if n%i == 0: return i
	return 1

def solve(n, j):
	z = []
	for t in product(range(2), repeat=n-2):
		x = 1
		for d in t: x = 10 * x + d
		x = 10 * x + 1

		s = str(x)
		l = []
		for b in range(2, 11):
			d = divisor(int(s, b))
			if d == 1: break
			l.append(d)

		if len(l) == 9:
			z.append((x, ' '.join(str(d) for d in l)))
			if len(z) == j: break

	return z

f = fileinput.input()
for t in range(int(f.readline().rstrip())):
	n, j = map(int, f.readline().rstrip().split(' '))
	z = solve(n, j)
	print('Case #%s:' % (t + 1))
	for e in z: print('%d %s' % e)
