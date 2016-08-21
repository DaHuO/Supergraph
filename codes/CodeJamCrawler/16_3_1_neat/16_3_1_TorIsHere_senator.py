#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sort_n_check(total_senator, sorted_tuple):
	if total_senator <= 0:
		return False, sorted_tuple
		
	if sorted_tuple[0][1] >= sorted_tuple[1][1]:
		return float(sorted_tuple[0][1])/float(total_senator) > 0.5 , sorted_tuple
	else:
		count = 0
		while count + 1 < len(sorted_tuple):
			if (int(sorted_tuple[count][1]) < int(sorted_tuple[count+1][1])):
				temp = sorted_tuple[count]
				sorted_tuple[count] = sorted_tuple[count + 1]
				sorted_tuple[count + 1] = temp
			else:
				break
			count += 1
		return float(sorted_tuple[0][1])/float(total_senator) > 0.5 , sorted_tuple

def solve(cipher, cipher2):
	num_party = int(cipher)
	count = 0
	total_senator = 0
	num_seneator_list = cipher2.split( )
	num_seneator_tuple_list = list()
	for char in ascii_uppercase:
		if count < num_party:
			num_seneator_tuple_list.append((char, int(num_seneator_list[count])))
			total_senator += int(num_seneator_list[count])
		count = count + 1

	ans = ""
	sorted_tuple = sorted(num_seneator_tuple_list, key=lambda tup: tup[1], reverse=True)
	while total_senator > 0:
		
		# First Try
		sorted_tuple[0] = (sorted_tuple[0][0], sorted_tuple[0][1] - 1)
		leaving_senator = sorted_tuple[0][0]
		is_there_majoriity, sorted_tuple = sort_n_check(total_senator - 1, sorted_tuple)
		total_senator -=1
		ans += leaving_senator
			
		#Second Try
		row_back_tuple = list(sorted_tuple)
		sorted_tuple[0] = (sorted_tuple[0][0], sorted_tuple[0][1] - 1)
		leaving_senator = sorted_tuple[0][0]
		
		is_there_majoriity, sorted_tuple = sort_n_check(total_senator - 1, sorted_tuple)
		
		if is_there_majoriity:
			sorted_tuple = row_back_tuple
			ans += " "
		else:
			total_senator -=1
			ans += leaving_senator
			ans += " "
		
	return ans.strip()

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		cipher2 = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher, cipher2)))