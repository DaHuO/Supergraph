#!/usr/bin/env python3
import math
 		
def get_base_value(number, base):
	result = str(number)
	total = 0
	for count, i in enumerate(result[::-1]):
		total += (int(i) * (base**count))
	return total

def trials(n):
	for k in range(2**(n-1) + 1, 2**n, 2):
		yield ''.join(list(bin(k))[2:])

def is_prime(number, divisor):
	#optimize code, check for 2 first because its the only even odd number
	if( (number % 2) == 0):
		divisor.append(str(2))
		return False
	root = int(math.sqrt(number))
	for i in range(3, root + 1 , 2):
		if (( number % i ) == 0 ):
			divisor.append(str(i))
			return False
	return True

		

def run():
	input_file = open('jamcoin.in', 'r')
	output_file = open('jamcoin.out', 'w')
	first_line = input_file.readline() # read the first line of the content of the small.in file
	T = int(first_line) # convert the string file to integer
	for no in range(1, T+1):
		next_string = next(input_file)
		n = int(next_string.split(" ")[0])
		j = int(next_string.split(" ")[1])
		output_file.write('Case #{}:\n'.format(no))
		print('Case #{}:'.format(no))
		count = 0
		for value in trials(n):
			prime = False
			divisor = []
			for k in range(2,11):
				if (is_prime(get_base_value(value, k), divisor)):
					prime = True
					break
			if (prime):
				continue
			elif(count < j):
					count += 1
					output_file.write('{} {}\n'.format(value, ' '.join(divisor)))
					print('{} {}'.format(value, ' '.join(divisor)))
			
				

run()