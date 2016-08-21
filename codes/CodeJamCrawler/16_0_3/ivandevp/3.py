#!/usr/bin/python

import sys
from itertools import count, islice, product 

def generate_jamcoins(n, j):
	cases = ["1" + "".join(seq) + "1" for seq in product("01", repeat=n-2)]
	valid_cases = get_valid_cases(cases, j)
	print "Case #1:"
	get_answer(j, valid_cases)
	

def base_10_to_n(num_str, base):
	return int(num_str, base)


def is_prime(num):
    return num > 1 and all(num%i for i in islice(count(2), int(pow(num,0.5)-1)))


def get_valid_cases(cases, j):
	valid_cases = []
	for case in cases:
		valid = True
		factors = []
		for i in range(9):
			converted_number = base_10_to_n(case, i+2)
			is_prime_number = is_prime(converted_number)
			if (is_prime_number):
				valid = False
				break
			else:
				factors.append(get_factors(converted_number))
		if valid:
			valid_cases.append({'case': case, 'factors': factors}) 

		if len(valid_cases) > j + 1:
			break
	return valid_cases


def get_factors(n):    
	factors = []
	for i in range(2, int(pow(n,0.5) + 1)):
		if n % i == 0 and i != 1:
			factors.append(i)
			break
	return factors
    #return [i for i in range(1, int(n**0.5) + 1) if n % i == 0 and i != 1]


def get_answer(j, valid_cases):
	for i in range(j):
		case = valid_cases[i]
		factors = ' '.join([str(factor[0]) for factor in case['factors']])		
		print "%s %s" % (case['case'], factors)


#t = int(raw_input('# Test Cases : '))
t = int(sys.argv[1])
for i in range(t):
	#n = int(raw_input("N => "))
	n = int(sys.argv[2])
	#j = int(raw_input("J => "))
	j = int(sys.argv[3])
	generate_jamcoins(n, j)