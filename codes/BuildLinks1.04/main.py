#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexicalAnalysis_function import lexicalanalysis
from getGTP import getGTP
from partialIndexGeneration import createPartialIndex
# from detectLinks import detectLinks

import os
from os import listdir
from os.path import isfile, join
import collections
import time

class buildLinks(object):
	def __init__(self, input_folder, threshold):
		start = time.time()
		self.input_folder = input_folder
		self.threshold = threshold
		self.coderecords = {}
		self.coderecords = self.lexiAnalysis(input_folder)
		print 'finished lexical analysis'
		self.GTP = getGTP(input_folder)
		print 'finished GTP generation'
		print self.GTP
		print len(self.GTP)
		# print self.GTP
		self.saveGTP(self.GTP)
		# for i in self.coderecords.keys():
		# 	print i
		# 	print self.coderecords[i].keys()
		lexi_folder = 'test_results' + input_folder[input_folder.find('/'):] + '/lexi_results'
		self.partialIndex, self.codes = createPartialIndex(lexi_folder, self.GTP, self.threshold)
		# print 'finished partial index generation'
		# print 'start building links'
		# # print self.partialIndex
		# linksDetector = detectLinks(input_folder, self.codes, self.partialIndex, threshold, self.GTP)
		# print 'finished building links'
		end = time.time()
		timelength = end - start
		print "time spent:"
		print timelength



	def lexiAnalysis(self, input_folder):
		coderecords = {}

		input_files = self.getFiles(input_folder)
		for f in input_files:
			coderecords[f[:f.rfind('.')]] = {}
			path = input_folder + '/' + f
			lexianalysis = lexicalanalysis(path)
			record = lexianalysis.getAnalysisResults()
			file_out = open('test_results' + input_folder[input_folder.find('/'):] + '/lexi_results/' + f[:f.rfind('.')] + '_lexi.txt','w')
			for line in record.keys():

				out = ''
				for part in record[line]:
					out += part + ' '
					# output += part[1] + ' '
				file_out.write(out + '\t\t' + str(line[0]) + ' ' + str(line[1]) + '\n')
				coderecords[f[:f.rfind('.')]][line] = record[line]
			file_out.close()
		return coderecords


	def getFiles(self, folder):
		target_path = folder
		target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
		if '.DS_Store' in target_files: 
			target_files.remove('.DS_Store')
		return target_files

	def saveGTP(self, GTP):
		file_out = open('test_results' + self.input_folder[self.input_folder.find('/'):] + '/GTP.txt', 'w')
		print 'saving'
		for token in GTP:
			file_out.write(token + '\t\t')
		file_out.close()


if __name__ == '__main__':
	input_folder = 'test_input/sort_codes'
	# input_folder = 'test_input/CodeJam/2A/python'
	threshold = 0.8
	buildlinks = buildLinks(input_folder, threshold)


