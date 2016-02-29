#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a funciton to compare two strings, returning the length difference
# and the minimum hamming difference(considering upper case and lower case are
# the same)

def StrDistance(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	if len1 >= len2:
		pass
	else:
		str1, str2 = str2, str1
		len1,len2 = len2,len1
	str1 = str1.lower()
	str2 = str2.lower()
	len_diff = len1 - len2
	ham_diff = 1024
	for i in range(0, len_diff + 1):
		temp_diff = 0
		for j in range(0, len2):
			# temp_diff += abs(ord(str1[j+i]) - ord(str2[j]))
			if str1[j+i] != str2[j]:
				temp_diff += 1
		if temp_diff<ham_diff:
			ham_diff = temp_diff
	return len_diff, ham_diff