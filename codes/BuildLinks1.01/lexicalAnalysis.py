#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tokenize
import re
import string
import collections

class lexicalanalysis():
	def __init__(self, test_input_folder, test_input_file):
		file_in = open('test_input/' + test_input_folder + '/' + test_input_file, 'r')
		self.test_input_folder = test_input_folder
		self.test_input_file = test_input_file
		self.main(file_in)

	def lexicalAnalysis(self, file_in):
		record = {}
		current_line = 0
		def handle_token(type, token, (srow, scol), (erow, ecol), line):
			if tokenize.tok_name[type] == 'COMMENT':
				pass
			else:
				# if srow == current_line:
				# 	record[srow].append([scol, token])
				# else:
				# 	record[srow] = []
				# 	record[srow].append([scol, token])
				# 	current_line += 1
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
		d = collections.OrderedDict(sorted(record.items()))
		# for key in record.keys():
		# 	print record[key]
		# for i in d:
		# 	print i

		# print record





		# count = 0
		# for line in file_in:
		# 	# print line
		# 	count += 1
		# 	line = line.strip()
		# 	if len(line)==0:
		# 		continue
		# 	print line
		# 	while line.find('  ')!=-1:
		# 		line = string.replace(line, '  ', ' ')
		# 	record.append(line + '\t\t' + str(count))
		# 	def handle_token(type, token, (srow, scol), (erow, ecol), line):
		# 		if tokenize.tok_name[type] == 'COMMENT':
		# 			return
		# 		else:
		# 			print token
		# 	# def return_line():
		# 	# 	inside_count = 0
		# 	# 	while inside_count < 1:
		# 	# 		yield line
		# 	# 		inside_count += 1
		# 	return_line = iter([line])
		# 	tokenize.tokenize(return_line, handle_token)

		file_in.close()
		# for line in record:
		# 	print line
		file_out = open('test_temp/lexi_results/' + self.test_input_file[:-3] + '_lexi.txt', 'w')
		for line in collections.OrderedDict(sorted(record.items())):
			output = ''
			for part in record[line]:
				output += part[1] + ' '
			file_out.write(output + '\t\t' + str(line) + '\n')
		file_out.close()

	def main(self, file_in):
		self.lexicalAnalysis(file_in)


if __name__ == '__main__':
	test_input_folder = 'sort_codes'
	test_input_file = 'Arraysort.py'
	lAnalysis = lexicalanalysis(test_input_folder, test_input_file)