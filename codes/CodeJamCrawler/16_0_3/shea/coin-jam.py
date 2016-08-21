#!/usr/bin/env python3

import re
from math import sqrt

COIN_RE = re.compile(r'^1(?:[01]+1)?$')


def isprime(n):
	n = abs(int(n))

	# 0 and 1 are not prime
	if n < 2:
		return False

	# 2 is prime and even
	if n == 2:
		return True

	# all other even numbers are not prime
	if n % 2 == 0:
		return False

	# beginning at 3, check all odd numbers up to sqrt(n)
	for x in range(3, int(sqrt(n) + 1), 2):
		if n % x == 0:
			return False

	return True


def isjamcoin(coin):

	# ensure is in the correct format
	if not re.match(COIN_RE, coin):
		return False

	# ensure it is not prime in bases 2-10
	for base in range(2, 11):
		if isprime(int(coin, base=base)):
			return False

	return True


def generate_coins(line):
	n, j = [int(n) for n in line.split(' ')]
	length, count = (n, j)

	coins = {}
	num = int('1' + '0' * (length-2) + '1', 2)
	limit = int('1' * length, 2)

	while num <= limit and len(coins) < count:
		coin = '{0:b}'.format(num)

		if not isjamcoin(coin):
			num += 1
			continue

		factors = []

		for i in range(1, 10):
			n = int(coin, i + 1)
			factor = 2
			while factor < n//2:
				if n % factor == 0:
					break
				factor += 1
			factors.append(str(factor))

		coins[coin] = ' '.join(factors)
		num += 1

		check(coin, coins[coin])

	return ''.join('\n{} {}'.format(coin, factors) for coin, factors in coins.items())


def check(num, factors):
	for i, factor in enumerate(factors.split()):
		n = int(num, i + 2)
		if n % int(factor) != 0:
			raise Exception('Error with result {} {}', num, factors)


def test(func, filename):
	input_file = open('tests/' + filename + '.in')
	output_file = open('tests/' + filename + '.out', 'w')
	lines = input_file.readlines()

	cases = int(lines[0])

	for case in range(1, cases + 1):
		line = lines[case].strip()
		result = func(line)
		print('Case #{}:{}'.format(case, result), file=output_file)

if '__main__' == __name__:
	test(generate_coins, 'C-small-attempt0')


