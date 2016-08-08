#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tokenize
import re
import string
import collections

class lexicalanalysis():
	def __init__(self, input_file):
		file_in = open(input_file, 'r')
		self.input_file = input_file
		self.record = self.lexicalAnalysis(file_in)

	def lexicalAnalysis(self, file_in):
		record = {}
		current_line = 0
		def handle_token(type, token, (srow, scol), (erow, ecol), line):
			if tokenize.tok_name[type] == 'COMMENT':
				pass
			else:
				token = token.strip()
				if len(token) == 0:
					return
				if token[:3] == '"""' or token[:3] == "'''":
					return
				if srow in record:
					record[srow].append([scol, token])
				else:
					record[srow] = []
					record[srow].append([scol, token])
		tokenize.tokenize(file_in.readline, handle_token)
		file_in.close()
		return record

	def getAnalysisResults(self):
		return self.record



if __name__ == '__main__':
	test_input_folder = 'sort_codes'
	test_input_file = 'Arraysort.py'
	lAnalysis = lexicalanalysis(test_input_folder, test_input_file)