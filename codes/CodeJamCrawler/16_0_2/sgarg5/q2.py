import sys
from sets import Set
from math import sqrt

plus_sign = '+'
minus_sign = '-'

def get_cont_minus(input_str):
	count = 0
	first = 0
	while len(input_str) > first and input_str[first] == minus_sign:
		first = first + 1
		count = count + 1
	return count

def get_cont_plus(input_str):
	first = 0
	count = 0
	while len(input_str) > first and input_str[first] == plus_sign:
		first = first + 1
		count = count + 1
	return count

def calc_min(input_str):
	global plus_sign, minus_sign

	no = len(input_str)
	last = no - 1
	op_count = 0

	while len(input_str) > 0:
		last = len(input_str) - 1
		if input_str[last] == minus_sign:
			minus_count = get_cont_minus(input_str)
			if minus_count != 0:
				op_count = op_count + 1
				input_str = input_str[minus_count:]
			else:
				plus_count =  get_cont_plus(input_str)
				op_count = op_count + 2
				input_str = input_str[plus_count:]

			input_str = input_str[::-1]
			"""
			if plus_sign == '-' and last == 0 and input_str[last] == '-':
				return op_count
			"""
			temp_sign = plus_sign
			plus_sign = minus_sign
			minus_sign = temp_sign
		else:
			input_str = input_str[:-1]
	return op_count

t = input()
for i in range(t):
	input_str = raw_input()
	plus_sign = '+'
	minus_sign = '-'
	print "Case #%d: %d" %(i+1, calc_min(input_str))