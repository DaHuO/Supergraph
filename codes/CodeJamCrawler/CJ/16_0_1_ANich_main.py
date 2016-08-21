#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(ciper):
	seen = []
	full_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	count = 1
	number = int(cipher)
	if number == 0:
		return 'INSOMNIA'
	while seen != full_list:
		product = number * count
		split_number = list(str(product))
		new_numbers = set(split_number) - set(seen)
		seen = seen + list(new_numbers)
		seen = sorted(seen)
		count += 1
	return str(product)
	

	
if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))

