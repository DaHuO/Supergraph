#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import collections
import math

def createPartialIndex(lexi_folder, GTP, threshold):
	lexi_files = getFiles(lexi_folder)
	I = {}
	C = {}
	for f in lexi_files:
		# print f
		C[f[:f.rfind('_')]] = {}
		file_in = lexi_folder + '/' + f
		lexi_in = open(file_in, 'r')
		for line in lexi_in:
			flag = line.rfind('\t\t')
			data = line[:flag].split(' ')
			data.remove('')
			lineNum = int(line[flag+2:])
			data.sort(key = lambda x: GTP.index(x))
			C[f[:f.rfind('_')]][lineNum] = data
			n = int(len(data) - math.ceil(len(data) * threshold) + 1)
			for i in range(n):
				t = data[i]
				if len(t)==0:
					continue
				if t in I.keys():
					I[t].append((t, i, f[:f.rfind('_lexi')], lineNum))
				else:
					I[t] = []
					I[t].append((t, i, f[:f.rfind('_lexi')], lineNum))
	return I, C

def readFromFile(file_in):
	file_in = open(file_in, 'r')
	file_in = file_in.read()
	GTP = []
	data_set = file_in.split('\t\t')
	for data in data_set:
		GTP.append(data)
	return GTP

def getFiles(folder):
	target_path = folder
	target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
	if '.DS_Store' in target_files: 
		target_files.remove('.DS_Store')
	return target_files

if __name__ == '__main__':
	file_in = 'test_results/sort_codes/GTP.txt'
	lexi_folder = 'test_results/sort_codes/lexi_results'
	threshold = 0.8
	GTP = readFromFile(file_in)
	createPartialIndex(lexi_folder, GTP, threshold)