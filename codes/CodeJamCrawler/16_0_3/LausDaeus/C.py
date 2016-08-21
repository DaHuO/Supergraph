import os
import sys
current = os.getcwd()
outer = os.path.dirname(os.getcwd())
sys.path.append(current)
sys.path.append(outer)

from utils.io import *

def main():
	start = time_in_ms()
	info = parse_data()
	raw_tests = info[0]
	output_file = info[1]
	results = []

	for r_test in raw_tests:
		test = [int(r_test[0]), int(r_test[1])]
		#test.append([int(g) for g in r_test[1]])
		results.append(solve(test))
		#print ""

	data_output(results, output_file)
	print "Time taken:",str(time_in_ms() - start)+"ms"

def solve(test):

	N = test[0]
	N_s = N-2
	required = test[1]
	result = []

	for i in xrange (0, 2**N_s):
		bits = bitfield(i)
		bits = [1]+[0]*(N_s-len(bits))+bits+[1]
		divisors = []

		for i in xrange(2,11):
			value = base_10(bits, i)
			#print bits
			#print value
			div = is_not_prime(value)
			if div:
				divisors.append(div)
			else:
				break

		if len(divisors) == 9:
			match = ''.join([str(b) for b in bits])+' '+' '.join([str(d) for d in divisors])
			print match
			result.append(match)

			if len(result) >= required:
				break


	print "Total found:",len(result)
	return '\n'+'\n'.join(result)

#Borrowed from stack overflow
def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

def base_10(bits, base):
	total = 0
	for idx, bit in enumerate(reversed(bits)):
		total += bit*base**idx
	return total

def is_not_prime(number):
	#divisors = int(number**0.5)+1
	for i in range(2,10):
		if i > 10:
			return False

		if number % i == 0:
			return i

	return False
if __name__ == '__main__':
	main()