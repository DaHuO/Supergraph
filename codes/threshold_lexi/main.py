#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexicalAnalysis_function import lexicalanalysis
from getRepresentations import getReps

import os
from os import listdir
from os.path import isfile, join
import collections
import time

def main(input_folder):
	threshold = 0.8
	files = getFiles(input_folder)
	coderecords = {}
	GTPrecords = {}
	for f in files:
		path = input_folder + '/' + f
		file_in = open(path, 'r')
		lexi = lexicalanalysis(path)
		records, GTP = lexi.getAnalysisResults()
		if len(records) == 0:
			continue
		coderecords[f[:f.rfind('.')]] = {}
		for line in records.keys():
			coderecords[f[:f.rfind('.')]][line] = records[line]
		for token in GTP:
			GTPrecords[token] = GTPrecords.get(token, 0) + GTP[token]
	L = sorted(GTPrecords.iteritems(), key = lambda (k, v): (v, k))
	x = [key for (key, value) in L]
	n = len(x)
	mt = int(n*threshold)
	print x

	limit = GTPrecords[x[mt]] - 1
	print n
	print mt
	print limit
	majortoken = set()
	for token in GTPrecords.keys():
		if GTPrecords[token] > limit:
			majortoken.add(token)
			print token
	print len(majortoken)

	countBlock = 0
	countYes = 0

	for code in coderecords.keys():
		countblock, countyes = getReps(coderecords[code], majortoken, threshold)
		countBlock += countblock
		countYes += countyes

	print countBlock, countYes





def getFiles(folder):
	target_path = folder
	target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
	if '.DS_Store' in target_files: 
		target_files.remove('.DS_Store')
	return target_files



if __name__ == '__main__':
	# input_folder = 'test_input/sort_codes'
	input_folder = 'test_input/CodeJam/2A/python'
	main(input_folder)