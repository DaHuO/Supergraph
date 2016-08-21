#!/usr/bin/env python3


def count_sheep(n):
	if n == 0:
		return 'INSOMNIA'

	digits = list(range(0, 10))
	count = 0

	while digits:
		count += 1

		for digit in str(n * count):
			digit = int(digit)
			if digit in digits:
				digits.remove(digit)

	return count * n


def test(func, filename):
	input_file = open(filename + '.in')
	output_file = open(filename + '.out', 'w')
	lines = input_file.readlines()

	cases = int(lines[0])

	for case in range(1, cases + 1):
		number = int(lines[case].strip())
		result = func(number)
		print('Case #{}: {}'.format(case, result), file=output_file)

test(count_sheep, 'A-large')
