#!/usr/bin/env python

import sys

# ==============================================================================
def read_input(filename):
	n = None
	cases = []
	with open(filename, 'r') as f:
		lines = [int(i) for i in f.read().strip().splitlines()]
		n = lines[0]
		cases = lines[1:]
	return n, cases

# ==============================================================================
def handle_case(case):
	digits = set()

	t = 0
	x = None
	while t <= 100 and len(digits) < 10:
		t += 1
		x = case * t

		digits.update([d for d in str(x)])

	return x if len(digits) == 10 else 'INSOMNIA'

# ==============================================================================
def main(filename):
	n, cases = read_input(filename)

	assert n == len(cases)

	with open('out.txt', 'w') as out:
		for i, case in enumerate(cases):
			result = handle_case(case)

			print i + 1, case, result

			out.write('Case #{}: {}\n'.format(i + 1, result))

# ==============================================================================
if __name__ == '__main__':
	main(*sys.argv[1:])
