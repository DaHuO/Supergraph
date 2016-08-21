#!/usr/bin/env python

import sys
import itertools

# Previously calculated results.
small_results = []
large_results = []

# ==============================================================================
def read_input(filename):
	t = None
	n = None
	j = None

	with open(filename, 'r') as f:
		t = int(f.readline().strip())
		n, j = [int(i) for i in f.readline().strip().split()]

	return t, n, j

# ==============================================================================
def write_line(out, coin, divisors):
	out.write('{} {}\n'.format(coin, ' '.join([str(d) for d in divisors])))

# ==============================================================================
def known_divisor(coin, base):
	if not hasattr(known_divisor, 'divs'):
		known_divisor.divs = {}

	val = int(coin, base)

	if val in known_divisor.divs:
		return known_divisor.divs[val]

	i = 2
	while i < min(((val / 2) + 2), 10000):
		if val % i == 0:
			known_divisor.divs[val] = i
			return i
		i += 1

	# Possibly prime.
	known_divisor.divs[val] = None
	return None

# ==============================================================================
def get_divisors(coin):
	divisors = [known_divisor(coin, base) for base in range(2, 11)]
	return None if None in divisors else divisors

# ==============================================================================
def main(filename):
	t, n, j = read_input(filename)

	assert t == 1

	found = 0
	with open('out.txt', 'w') as out:
		out.write('Case #1:\n')

		for coin in itertools.product('01', repeat = n - 2):
			coin = '1{}1'.format(''.join(coin))

			divisors = get_divisors(coin)
			if divisors:
				write_line(out, coin, divisors)

				found += 1
				if found == j:
					return

# ==============================================================================
if __name__ == '__main__':
	main(*sys.argv[1:])
