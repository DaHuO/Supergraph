#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
'''
LIMIT = 16
base_two = [math.pow(2, x) for x in range(LIMIT)]
base_three = [math.pow(3, x) for x in range(LIMIT)]
base_four = [math.pow(4, x) for x in range(LIMIT)]
base_five = [math.pow(5, x) for x in range(LIMIT)]
base_six = [math.pow(6, x) for x in range(LIMIT)]
base_seven = [math.pow(7, x) for x in range(LIMIT)]
base_eight = [math.pow(8, x) for x in range(LIMIT)]
base_nine = [math.pow(9, x) for x in range(LIMIT)]
base_ten = [math.pow(10, x) for x in range(LIMIT)]
'''

def derive_ans(answer):
	derived_ans = "\n"
	for ans in answer:
		derived_ans = derived_ans + ans + "\n"
	return derived_ans

def get_nontrivial_divisors(num):
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return i
	return 0

def solve(cipher):
	n, j = cipher.split( )
	possible_case = int(math.pow(2, int(n) - 2))
	ans = []
	for i in range(possible_case):
		check_seq = bin(i)[2:].zfill(int(n) - 2)
		check_seq = '1' + check_seq + '1'

		nontrivial_divisors = ""
		is_valid = True
		for k in xrange(2, 11):
			divisors = get_nontrivial_divisors(int(check_seq, k))
			if divisors == 0:
				is_valid = False
				break
			else:
				nontrivial_divisors = nontrivial_divisors + str(divisors) + " "

		if is_valid:
			ans.append(check_seq + " " + nontrivial_divisors)
		if len(ans) == int(j):
			return derive_ans(ans)

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))

