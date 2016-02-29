#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import StrDistance

def getinputdata(file):
	datadic = {}
	for line in file:
		flag = line.find("',")
		string = line[2:flag]
		count = line[flag + 2:-2]
		datadic[string] = int(count)
	return datadic


Hamdiff_Threshold = 1
Lendiff_Threshold = 1

File1 = open('../HuffmanString/test_results/httpd_word.txt', 'r')
File2 = open('../HuffmanString/test_results/GoHttp_word.txt', 'r')

data1 = getinputdata(File1)
data2 = getinputdata(File2)
File1.close()
File2.close()
File_out = open('test_results/test_result_1_1.txt', 'w')
for word1 in data1:
	if len(word1)==1:
		continue
	for word2 in data2:
		if len(word2)==1:
			continue
		print word1, word2
		len_diff, ham_diff = StrDistance.StrDistance(word1, word2)
		print len_diff
		if ham_diff<=Hamdiff_Threshold and len_diff<=Lendiff_Threshold:
			result = 'data1: ' + word1 + ' ' + str(data1[word1]) + \
			'\t\t\tdata2: ' + word2 + ' ' + str(data2[word2]) + '\n'
			File_out.write(result)
File_out.close()
