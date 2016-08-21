import sys
from sets import Set
from math import sqrt

t = input()
input_string = raw_input().split(" ")
N = int(input_string[0])
J = int(input_string[1])

coin = 1
coin = coin << (N - 1)
coin = coin + 1
unique_set = Set([])
output_map = {}

def check_prime(number):
	a = 2
	while (sqrt(number) + 1) > a:
		if number % a == 0:
			return a
		a = a + 1
	return -1

def check_validity(coin):
	coin =  bin(coin)[2:]
	list_divisor = []
	for base in range(2,11):
		converted_number = int(coin, base)

		op = check_prime(converted_number)
		if op == -1:
			return
		else :
			list_divisor.append(op)

	output_map[coin] = list_divisor
	if len(output_map.keys()) == J:
		for key, value in output_map.items():
			value = [str(ele) for ele in value]
			value = " ".join(value)
			print key, value
		sys.exit()

def generate_numbers(coin, start):
	for i in range(start, N-1):
		generate_numbers(coin, start + 1)
		new_coin = (1 << (N - 1 - start)) | coin
		generate_numbers(new_coin, start + 1)
	
	if coin not in unique_set:
		unique_set.add(coin)
		check_validity(coin)

print "Case #1:"
generate_numbers(coin, 1)
