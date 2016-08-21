#!/usr/bin/env python3


def last_index(l, value):
	for i, v in enumerate(reversed(l)):
		if v == value:
			return len(l) - 1 - i
	return -1


def done(stack):
	for pancake in stack:
		if pancake == '-':
			return False
	return True


def flip(stack, height):
	top = stack[:height]
	bottom = stack[height:]

	top = list(top)
	for i in range(0, height):
		top[i] = ('+' if top[i] == '-' else '-')

	top.reverse()

	return ''.join(top) + bottom


def sort_pancakes(stack):
	flips = 0

	while not done(stack):

		if stack[0] == '+':
			stack = flip(stack, stack.index('-'))
		else:
			stack = flip(stack, last_index(stack, '-') + 1)

		flips += 1

	return flips


def test(func, filename):
	input_file = open('tests/' + filename + '.in')
	output_file = open('tests/' + filename + '.out', 'w')
	lines = input_file.readlines()

	cases = int(lines[0])

	for case in range(1, cases + 1):
		line = lines[case].strip()
		result = func(line)
		print('Case #{}: {}'.format(case, result), file=output_file)


test(sort_pancakes, 'B-large')
