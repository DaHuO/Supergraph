import math
from random import randint

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

print("Case #1:")

# Check if a number is prime
def is_prime_number (number):
	# prime numbers are greater than 1
	if (number > 1):
		for i in xrange(2, int(number**0.5) + 1):
			"""if variable number divided by any number greater than 1 and smaller than that variable number gets rest = 0, 
			than it`s not a prime number""" 
			if (int(number) % i == 0): 
				return False
		return True	
	else:
		return False

# return the number in base X
def base_x (sequence, x):
	base_number = 0;
	for i in xrange(0, len(sequence)):
		if (sequence[i] == "1"):
			base_number += math.pow(x, len(sequence) - i - 1)
	return base_number

# return one non trivial divisor for that number
def non_trivial_divisor (number):
	for i in xrange(2, number):
		if (number % i == 0):
			return i

def generate_sequence (n,last_sequence):
	# jam coin string
	sequence_change = last_sequence[1:-1]
	sequence_change = str(bin(int(sequence_change,2) + int("1",2)))[2:]
	if (len(sequence_change) < (n-2)):
		sequence_change = "0"*(n-2-len(sequence_change)) + sequence_change
	sequence = "1" + sequence_change + "1"
	# print(sequence)
	return sequence

for i in xrange(1, t + 1):
	n, j = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	jamCoins = 0
	last_sequence = "1" + (n-2)*"0" + "1"
	while (jamCoins < j):
		sequence = generate_sequence(n,last_sequence)
		last_sequence = sequence
		is_valid = True
		for x in xrange(2,11):
			if (is_prime_number(int(base_x(sequence, x)))):
				is_valid = False		
				break
		if (is_valid):
			#jamCoins.append(sequence)
			jamCoins+=1
			non_triv_div = ""
			for div in xrange(2,11):
				non_triv_div += str(non_trivial_divisor(int(base_x(sequence, div)))) + " "
			non_triv_div = non_triv_div[:-1]
			print(sequence + " " + non_triv_div)