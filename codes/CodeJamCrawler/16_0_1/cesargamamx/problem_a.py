#!/usr/bin/python
"""
Google Code Jam 2016
Problem A. Counting Sheep

https://code.google.com/codejam/contest/6254486/dashboard
"""


def mark_digit(number, digits):
	"""Mark the digits seen.
	
	We are using a list to keep counts on what digits we have seen so far, this
	function sets to 1 the index of the digit we have already seen.
	"""
	number = str(number)
	for digit in number:
		digits[int(digit)] = 1
	return digits

    
def evaluate_case(n):
	"""Evaluate a case
	
	Uses mark_digit() to get the last number seen before failling asleep
	"""
	if n:
		i = 1
		digits = [0 for x in range(10)]
		while sum(mark_digit(i*n, digits)) < 10:
			i += 1
		return i*n
	else:
		return "INSOMNIA"


def main():
	"""Main function
	
	Read the number of cases and the starting number
	"""
	t = int(raw_input())
	for i in xrange(1, t + 1):
  		n = int(raw_input())
  		print "Case #{}: {}".format(i, evaluate_case(n))


if __name__ == "__main__":
	main()
