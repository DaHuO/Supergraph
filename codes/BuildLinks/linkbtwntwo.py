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


Hamdiff_Threshold = 0
Lendiff_Threshold = 0

File1_name = 'httpd'
File2_name = 'GoHttp'

File1 = open('../HuffmanString/test_results/' + File1_name+ '_word.txt', 'r')
File2 = open('../HuffmanString/test_results/' + File2_name+ '_word.txt', 'r')

data1 = getinputdata(File1)
data2 = getinputdata(File2)
File1.close()
File2.close()
File_out = open('test_results/' + File1_name + '_' + File2_name + \
	str(Hamdiff_Threshold) + '_' + str(Lendiff_Threshold) + '.txt', 'w')
firstline = 'First code: ' + File1_name + '\t\t\t' + 'Second code: ' \
+ File2_name + '\n'
secondline = 'Hamdiff_Threshold: ' + str(Hamdiff_Threshold) + \
'\t\t\tLendiff_Threshold: ' + str(Lendiff_Threshold) + '\n\n\n'
File_out.write(firstline)
File_out.write(secondline)

for word1 in data1:
	if len(word1)==1:
		continue
	for word2 in data2:
		if len(word2)==1:
			continue
		len_diff, ham_diff = StrDistance.StrDistance(word1, word2)
		if ham_diff<=Hamdiff_Threshold and len_diff<=Lendiff_Threshold:
			result = 'data1: ' + word1 + ' ' + str(data1[word1]) + \
			'\t\t\tdata2: ' + word2 + ' ' + str(data2[word2]) + '\n'
			File_out.write(result)
File_out.close()
