#!/bin/python3

from sys import argv

DECIMAL_DIGITS = set(range(10))

def answer(n):
	if not n:
		return "INSOMNIA"

	seen_digits = set()
	seen_nums = set()

	i = 1

	while True:
		seen_nums.add(i*n)

		seen_digits |= digits(i*n)

		if seen_digits == DECIMAL_DIGITS:
			return max(seen_nums)

		i += 1

def digits(num):
	"""
	Computes the set of digits in an integer
	"""
	return set(map(int, str(num)))

def main():
	printer = AnswerPrinter()

	with open(argv[1], "r") as f:
		for words in parse_file(f):
			printer.print_answer(answer(words))

def parse_file(f):
	"""
	Generates items parsed from a file
	"""
	T = int(f.readline())

	for line in f:
		yield parse_num(line)

def parse_num(line):
	"""
	Parses a number from a line
	"""
	return int(line.strip())


class AnswerPrinter:
	"""
	Class to assist in printing out test case results
	"""
	def __init__(self): self.i = 1

	def print_answer(self, answer):
		"""
		Prints an answer prefixed by the test case #
		"""
		print("Case #%d: %s" % (self.i, answer))
		self.i += 1


if __name__ == "__main__":
	main()