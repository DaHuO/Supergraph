# Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. 
# First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on.
# Whenever she names a number, she thinks about all of the digits in that number.
# She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at
# least once so far as part of any number she has named.
# Once she has seen each of the ten digits at least once, she will fall asleep.

# Bleatrix must start with N and must always name (i + 1) × N directly after i × N.
# For example, suppose that Bleatrix picks N = 1692. She would count as follows:

#      N = 1692. Now she has seen the digits 1, 2, 6, and 9.
#     2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
#     3N = 5076. Now she has seen all ten digits, and falls asleep.

# What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead. 

from bitarray import bitarray

def has_all_digits(n):
	original_n = n
	digits = bitarray(10)
	for _ in range(100):
		for digit in extract_digits(n):
			digits[digit] = True
		if all(digits):
			return n
		n += original_n
	return 0

def extract_digits(n):
	while n:
		yield n % 10
		n //= 10

with open('A-large.in') as data:
	first = int(data.readline())
	for i in range(1, first + 1):
		line = int(data.readline())
		digits = has_all_digits(line)
		if digits:
			print("Case #%i: %i" % (i, digits))
		else:
			print("Case #%i: INSOMNIA" % i)