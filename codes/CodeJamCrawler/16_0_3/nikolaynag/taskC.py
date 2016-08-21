#!/usr/bin/env python
import sys

try:
    xrange
except NameError:
    xrange = range

def gen_primes(limit):
	primes = []
	is_prime = [True] * limit
	for n in xrange(2, limit):
		if is_prime[n]:
			primes.append(n)
			for i in range(n*n, limit, n):
				is_prime[i] = False
	return primes

PRIMES = gen_primes(1000)

def find_divisor(num):
	for d in PRIMES:
		if d > num**0.5: 
			return None
		if num % d == 0:
			return d
	return None
	
lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == 1)
assert(len(lines) == 2)
sN, _, sJ = lines[1].partition(" ")
N = int(sN)
J = int(sJ)

sys.stdout.write("Case #1:\n")
found = 0
for n in xrange(2**(N-2)-1, -1, -1):
	coin = "{:b}".format(2**(N-1) + 2*n + 1)
	divisors = []
	for i in range(2, 11, 1):
		d = find_divisor(int(coin, i))
		if d == None:
			break
		divisors.append(d)
	if len(divisors) < 9:
		continue
	sys.stdout.write(" ".join([coin] + [str(d) for d in divisors]) + "\n")
	found += 1
	if found >= J:
		break

assert(found >= J)
