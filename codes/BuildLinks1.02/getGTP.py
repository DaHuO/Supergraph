#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import listdir
from os.path import isfile, join
import collections

def getGTP(input_folder):
	path = 'test_results/' + input_folder[len('test_input'):] + '/lexi_results'
	input_files = getFiles(path)
	dic = {}
	for f in input_files:
		path = 'test_results/' + input_folder[len('test_input'):] + '/lexi_results/' + f
		File = open(path, 'r')
		for line in File:

			data_set = line.split('/t/t')[0].split(' ')
			for data in data_set:
				data = data.strip()
				if len(data)==0:
					continue
				if data in dic.keys():
					dic[data] += 1
				else:
					dic[data] = 1
	L = sorted(dic.iteritems(), key = lambda (k, v): (v, k))
	GTP = [key for (key, value) in L]
	GTP.append('')
	return GTP

def getFiles(folder):
	target_path = folder
	target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
	if '.DS_Store' in target_files: 
		target_files.remove('.DS_Store')
	return target_files

if __name__ == '__main__':
	GTP = getGTP('test_input/sort_codes')
	print GTP