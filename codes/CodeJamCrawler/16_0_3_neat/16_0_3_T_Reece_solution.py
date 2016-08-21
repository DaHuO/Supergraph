#!/usr/bin/python3

import itertools, re
#
#def prime_factors(n):
#	primfac = []
#	d = 2
#	while d*d <= n:
#		while (n % d) == 0:
#			primfac.append(d)  # supposing you want multiple factors repeated
#			n //= d
#		d += 1
#		if n > 1:
#			primfac.append(n)
#		return primfac

def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

def nonprime_factor(num, base):
	number = sum([int(num[len(num)-i-1]) * (base ** i) for i in range(len(num))])
	factors = prime_factors(number)
	if len(factors) == 1:
		return None
	return str(factors[0])

def solve(N,J):
	solved = 0
	for i in range((N-2)**2):
		num = '1' + bin(i)[2:].rjust(N-2,'0') + '1'
		npfs = [None] * 9
		works = True
		for i in range(2,11):
			npf = nonprime_factor(num, i)
			if not npf:
				works = False
			npfs[i-2] = npf
		if works:
			solved = solved + 1
			print(num, ' '.join(npfs))	
		if solved == J: # We got to the end!
			return

with open('input.txt', 'r') as f:
	num_problems = int(f.readline())
	for i in range(num_problems):
		N,J = [int(i) for i in f.readline().rstrip().split(' ')]
		print('Case #%s:' % (i+1))
		solve(N,J)
