#!/usr/bin/env python

from sys import stdin
from random import randrange
from fractions import gcd

def perm(n, i):
	return bin((1 << (n-1)) + (i << 1) + 1)[2:]

def miller_rabin(n, k=500):
	if n == 2:
		return (True, 0)
	if not n & 1:
		return (False, 2)

	def check(a, r, d, n):
		x = pow(a, d, n)
		if x == 1:
			return (True, 0)
		for i in xrange(r - 1):
			if x == n - 1:
				return (True, 0)
			x = pow(x, 2, n)
		return x == n - 1

	r = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		r += 1

	for i in xrange(k):
		a = randrange(2, n - 1)
		if not check(a, r, d, n):
			if gcd(pow(a, d, n) - 1, n) > 1:
				return (False, gcd(pow(a, d, n) - 1, n))
			elif gcd(pow(a, pow(2, r)*d, n) - 1, n) > 1:
				return (False, gcd(pow(a, pow(2, r)*d, n) - 1, n))
	return (True, 0)

def divisor(n):
	for i in range(2, n):
		if n % i == 0:
			return i

def jamcoin(n):
	divisors = []
	for i in range(2, 11):
		j = int(n, i)
		mr = miller_rabin(j)
		if mr[0]:
			return None
		divisors.append(mr[1])
	return [n, divisors]

def gen_coins(n, j):
	k = 0
	m = long(pow(2, n - 2))
	coins = []
	i = 0
	while i < m:
		c = perm(n, i)
		jc = jamcoin(c)
		if jc is not None:
			k += 1
			coins.append(jc)
		if k == j:
			break
		i += 1
	return coins

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	x = map(int, stdin.readline().rstrip('\n').split(' '))
	n = x[0]
	j = x[1]
	print "Case #%d:" % (i + 1)
	coins = gen_coins(n, j)
	print str(map(lambda c: str(c).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace('L', ''), coins)).replace('[', '').replace(']', '').replace("'", '').replace(', ', '\n')
