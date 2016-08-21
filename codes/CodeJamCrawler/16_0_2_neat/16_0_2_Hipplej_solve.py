#!/usr/bin/env python

import sys

# ==============================================================================
def read_input(filename):
	n = None
	cases = []
	with open(filename, 'r') as f:
		lines = [l.strip() for l in f.readlines()]
		n = int(lines[0])
		cases = lines[1:]
	return n, cases

# ==============================================================================
def handle_case(case):

	def solved(x):
		return '-' not in x

	def flip(x, i):
		assert i < len(x)

		return ''.join(['+' if p == '-' else '-' for p in x[:i + 1]]) + x[i + 1:]

	count = 0
	stack = case
	while not solved(stack):
		stack = flip(stack, stack.rfind('-'))

		count += 1

	return count

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
