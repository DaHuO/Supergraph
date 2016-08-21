# -*- coding: utf-8 -*-
#
# Copyright 2013 Eric Shtivelberg
#

import sys

problem = 'C-small-attempt0'


# # Open the input file
input_file_name = problem + '.in'
# input_file = open(input_file_name)
# lines = map(str.strip, input_file.readlines())
# input_file.close()

# print "Closed input file..."

lines = '''1
16 50'''.split('\n')


def read_line(): return lines.pop(0)
def read_parts(): return lines.pop(0).split(' ')
def read_int(): return int(lines.pop(0))
def read_ints(): return map(int, lines.pop(0).split(' '))
def read_float(): return int(lines.pop(0))
def read_floats(): return map(float, lines.pop(0).split(' '))

# Write the output
output_file_name = problem + '.out'
output_file = open(output_file_name, 'w')
# output_file = sys.stdout

########## Contest Specific ##########
base_cache = {b: {} for b in xrange(1, 11)}
def number2base(n, b):
	if n == 0:
		return [0]
	# elif n in base_cache[b]:
		# return base_cache[b][n]

	digits = []
	while n:
		digits.append(str(int(n % b)))
		n /= b

	# result = base_cache[b][n] = ''.join(digits[::-1])
	result = ''.join(digits[::-1])
	return result

import numpy as np
from numpy import array, bool_, multiply, nonzero, ones, put, resize
#
def makepattern(smallprimes):
	pattern = ones(multiply.reduce(smallprimes), dtype=bool_)
	pattern[0] = 0
	for p in smallprimes:
		pattern[p::p] = 0
	return pattern
#
def primes_upto3(limit, smallprimes=(2,3,5,7,11)):    
	sp = array(smallprimes)
	if limit <= sp.max(): return sp[sp <= limit]
	#
	isprime = resize(makepattern(sp), limit + 1) 
	isprime[:2] = 0
	put(isprime, sp, 1) 
	#
	for n in xrange(sp.max() + 2, int(limit**0.5 + 1.5), 2): 
		if isprime[n]:
			isprime[n*n::n] = 0 
	return nonzero(isprime)[0]

import gmpy2
import itertools

def primes2(table=None):
    # def sieve(limit):
        # sieve_limit = gmpy2.isqrt(limit) + 1
        # limit += 1
        # bitmap = gmpy2.xmpz(3)
        # bitmap[4 : limit : 2] = -1
        # for p in bitmap.iter_clear(3, sieve_limit):
            # bitmap[p*p : limit : p+p] = -1
        # return bitmap

    # table_limit=1000000
    # if table is None:
        # table = sieve(table_limit)

    # for n in table.iter_clear(10**15, 10**33):
        # yield n

	s = 2
	m = long(10) ** 16
	for n in itertools.count(s, 2):
		yield gmpy2.next_prime(n)

		if n > m:
			break

    # n = table_limit
    # while True:
        # n = gmpy2.next_prime(n)
        # yield n
# primes = list(primes2())


primes = primes_upto3(2**17)
# primes = tuple(rwh_primes2_python3(10**16))
# max_prime2 = primes[-2]
max_prime = primes[-1]
# print 'Done computation', len(primes)

def isPrime(n):
	next_prime = gmpy2.next_prime(n-1)
	return next_prime == n

# from math import sqrt
# from itertools import count, islice
# def isPrime(n):
	# if n <= max_prime:
		# return n in primes

	# return all(n%i for i in islice(count(1), int(sqrt(n)-1)))

# The output list
output = []

T = read_int()

for t in range(1, T+1):
	N, J = read_ints()
	# N = 4
	# N = 16
	# N = 32
	# J = 500

	max_jamcoin = 0
	for i in xrange(N):
		max_jamcoin += (1 << i)

	ii = 0

	jamcoins = []
	jamcoin = 1 + (1 << (N-1)) - 2
	while jamcoin < max_jamcoin and J > 0:
		jamcoin += 2

		# Check if prime in base 2
		# if jamcoin in primes:
		if isPrime(jamcoin):
			# print 2, jamcoin
			continue

		jamcoin_binary = number2base(jamcoin, 2)

		# Check if prime in base 3 to 10
		any_prime = False
		for b in xrange(3, 11):
			print int(jamcoin_binary, b)
			# if int(jamcoin_binary, b) in primes:
			if isPrime(int(jamcoin_binary, b)):
				# print b, jamcoin_binary
				any_prime = True
				break

		if any_prime:
			if ii % 10000:
				print ii, 'checked'

			continue

		J -= 1
		print J, 'left'

		nontrivial_divisors = []

		for b in xrange(2, 11):
			jamcoin_in_base = int(jamcoin_binary, b)
			divisor = None
			for p in primes:
				if jamcoin_in_base % p == 0:
					divisor = p
					break

				if p > jamcoin_in_base:
					raise Exception()

			if not divisor:
				p = gmpy2.mpz(long(max_prime))
				while jamcoin_in_base % p != 0 and p < jamcoin_in_base:
					p = gmpy2.next_prime(p)
				divisor = p

			# print b, jamcoin_in_base, divisor
			assert divisor < jamcoin_in_base and divisor, (divisor, jamcoin_in_base)

			nontrivial_divisors.append(str(divisor))

		# print number2base(jamcoin, 2), nontrivial_divisors
		jamcoins.append('{} {}'.format(number2base(jamcoin, 2), ' '.join(nontrivial_divisors)))
	# print number2base(max_jamcoin, 2)

	output.append('''
{}'''.format('\n'.join(jamcoins)))


########## Contest Specific End ##########

# print output
cases = ['Case #{}: {}'.format(i+1, output[i]) for i in range(len(output))]
output_file.write('\n'.join(cases))

output_file.close()
# print "Closed output file..."