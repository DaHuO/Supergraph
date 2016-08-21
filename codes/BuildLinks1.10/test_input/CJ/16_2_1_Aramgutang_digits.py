#!/usr/bin/env python

import sys

NUMBERS = (
	(
		('0', 'ZERO', 'Z'),
		('2', 'TWO', 'W'),
		('6', 'SIX', 'X'),
		('8', 'EIGHT', 'G'),
	),
	(
		('3', 'THREE', 'H'),
		('4', 'FOUR', 'R'),
	),
	(
		('1', 'ONE', 'O'),
		('5', 'FIVE', 'F'),
		('7', 'SEVEN', 'S'),
	),
	(
		('9', 'NINE', 'I'),
	)
)

def remove(input, number):
	for letter in number:
		index = input.index(letter)
		input = input[:index] + input[index+1:]
	return input

with open(sys.argv[1]) as f:
	f.readline()
	for case, line in enumerate(f, 1):
		input = line.strip()
		result = ''
		while input:
			for number_set in NUMBERS:
				for number, needle, unique in number_set:
					while unique in input:
						input = remove(input, needle)
						result += number
		print('Case #%s: %s' % (case, ''.join(sorted(result))))

