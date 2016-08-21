#!/usr/bin/python

import sys

def convert_to_all_bases(binary_string):
	b2 = int(binary_string, 2)
	b3 = int(binary_string, 3)
	b4 = int(binary_string, 4)
	b5 = int(binary_string, 5)
	b6 = int(binary_string, 6)
	b7 = int(binary_string, 7)
	b8 = int(binary_string, 8)
	b9 = int(binary_string, 9)
	b10 = int(binary_string, 10)
	return [b2, b3, b4, b5, b6, b7, b8, b9, b10]

def get_prime_factorization(number):
    primes = []
    d = 2
    while d*d <= number:
        while (number % d) == 0:
            primes.append(d) 
            number //= d
        d += 1
    if number > 1:
       primes.append(number)
    return primes

file_name = sys.argv[1]
fp = open(file_name)
contents = fp.read().splitlines()
contents[0] = int(contents[0])
contents[1] = [int(n) for n in contents[1].split()]

# Number of correct cases we need to find
total_cases = contents[1][1]

## The minimum value of the string in binary
min_binary_string = bin(2 ** (contents[1][0] - 1) + 1)[2:]
# For iteration purposes, store it as decimal
min_decimal = int(min_binary_string, 2)

# Begin counter of values we found
counter = 0
all_binaries_and_primes = []

# print convert_to_all_bases('1001')
while counter != total_cases:
	all_bases = convert_to_all_bases(min_binary_string)
	all_primes = map(lambda x:get_prime_factorization(x)[0], all_bases)
	matches = [i for i, j in zip(all_bases, all_primes) if i == j]
	# If the list is empty, this is a valid binary value
	if not matches:
		bin_and_primes = [min_binary_string] + all_primes
		all_binaries_and_primes.append(bin_and_primes)
		counter = counter + 1
	
	min_decimal = min_decimal + 2
	min_binary_string = bin(min_decimal)[2:]

print 'Case #1:'
for item in all_binaries_and_primes:
	print ' '.join(str(x) for x in item)

