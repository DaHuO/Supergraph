#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Qualification_Round_2016_a.py
#
#  Copyright 2016 nerio
#
#

import fileinput

def calc_sleep_num(N):
	
	missing_nums = [0, 1, 2, 3, 4, \
					5, 6, 7, 8, 9]
	m = 1
	
	if int(N) == 0:
		return 'INSOMNIA'
	
	while missing_nums:
		X = m * N
		for i in str(X):
			i = int(i)
			if i in missing_nums:
				missing_nums.remove(i)
		
		m += 1
	
	return X
	

def main():

	curr_t_case = 1
	first_line = True
	for line in fileinput.input():
		line = line.strip()
		
		if first_line:
			t_cases = int(line)
			first_line = False
			continue
		
		N = int(line)
		result = calc_sleep_num(N)
			
		print('Case #', curr_t_case ,': ', result, sep='')
		curr_t_case += 1

	return 0

if __name__ == '__main__':
	main()
