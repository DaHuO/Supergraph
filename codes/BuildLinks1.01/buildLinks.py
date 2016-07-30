#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexicalAnalysis import lexicalanalysis
from tokenCompare import tokenCompare
from corpus import Corpus

import sys
import os
from os import listdir
from os.path import isfile, join
import operator
import bisect


class buildlinks(object):
	def __init__(self, target):
		self.lexiAnalysis(target)
		self.corpus = self.createCorpus(target)
		print sys.getsizeof(self.corpus)
		mem = 0
		for key in self.corpus.keys():
			mem += sys.getsizeof(self.corpus[key])
		print mem
		self.buildLinks(target)

	def lexiAnalysis(self, target):
		target_files = self.getFiles(target)
		for target_file in target_files:
			temp = lexicalanalysis(target, target_file, False)

	def createCorpus(self, target):
		corpus = Corpus(target + '/lexi_results').getCorpus()
		return corpus

	def buildLinks(self, target):
		files = self.getFiles(target)
		keys = self.corpus.keys()
		# files_in = map(lambda x: x[:-3] + '_lexi.txt', files)
		for file_in in files:
			file_in = file_in[:file_in.rfind('.')]
			link_count = {}
			link_tuples = []
			lines = []
			print file_in
			file_path = 'test_temp/' + target + '/lexi_results/' + file_in + '_lexi.txt'
			lexi_in = open(file_path, 'r')
			lexi_out = open('test_temp/' + target + '/link_results/' + file_in + '_link.txt', 'w')
			for line in lexi_in:
				line = line.strip()
				flag = line.rfind('\t\t')
				body = line[:flag].split(' ')
				body.remove('')
				if len(body)<=1:
					continue
				if body in lines:
					continue
				else:
					lines.append(body)
				lineNum = line[flag+2:]
				if body[0][0] in keys:
					key = body[0][0]
					flag = self.biSearch(self.corpus[key], body)
					# print flag
					if flag == -1:
						continue
					else:
						if self.corpus[key][flag][1] != file_in and tokenCompare(body, self.corpus[key][flag][0]):
							link_tuple = (lineNum, self.corpus[key][flag][1], self.corpus[key][flag][2])
							if link_tuple in link_tuples:
								pass
							else:
								link_tuples.append(link_tuple)
								if self.corpus[key][flag][1] in link_count.keys():
									link_count[self.corpus[key][flag][1]] += 1
								else:
									link_count[self.corpus[key][flag][1]] = 1
								lexi_out.write(lineNum + '\t\t' + self.corpus[key][flag][1] + '\t\t' + str(self.corpus[key][flag][2]) + '\n')
						left = flag - 1
						right = flag + 1
						if left<0:
							pass
						else:
							while(left >= 0 and self.corpus[key][left][0][0]==body[0]):
								# print body, '==left==', left, self.corpus[key][left][0]
								if self.corpus[key][left][1] != file_in and tokenCompare(body, self.corpus[key][left][0]):
									link_tuple = (lineNum, self.corpus[key][left][1], self.corpus[key][left][2])
									if link_tuple in link_tuples:
										pass
									else:
										link_tuples.append(link_tuple)
										if self.corpus[key][left][1] in link_count.keys():
											link_count[self.corpus[key][left][1]] += 1
										else:
											link_count[self.corpus[key][left][1]] = 1
										lexi_out.write(lineNum + '\t\t' + self.corpus[key][left][1] + '\t\t' + str(self.corpus[key][left][2]) + '\n')
								left = left - 1
						if right >len(self.corpus[key]) - 1:
							pass
						else:
							while(right <= len(self.corpus[key]) - 1 and self.corpus[key][right][0][0]==body[0]):
								# print body, '==right==', right, self.corpus[key][right][0]
								if self.corpus[key][right][1] != file_in and tokenCompare(body, self.corpus[key][right][0]):
									link_tuple = (lineNum, self.corpus[key][right][1], self.corpus[key][right][2])
									if link_tuple in link_tuples:
										pass
									else:
										link_tuples.append(link_tuple)
										if self.corpus[key][right][1] in link_count.keys():
											link_count[self.corpus[key][right][1]] += 1
										else:
											link_count[self.corpus[key][right][1]] = 1
										lexi_out.write(lineNum + '\t\t' + self.corpus[key][right][1] + '\t\t' + str(self.corpus[key][right][2]) + '\n')
								right += 1
						# lexi_out.write(str(left)+ ' '+str(flag)+ ' '+str(right)+'\n')
						# print left, flag, right

					# for corp in self.corpus[body[0][0]]:
					# 	if corp[1] != file_in and tokenCompare(body, corp[0]) :
							# link_tuple = (lineNum, corp[1], corp[2])
							# if link_tuple in link_tuples:
							# 	continue
							# else:
							# 	link_tuples.append(link_tuple)
							# 	if corp[1] in link_count.keys():
							# 		link_count[corp[1]] += 1
							# 	else:
							# 		link_count[corp[1]] = 1
							# 	lexi_out.write(lineNum + '\t\t' + corp[1] + '\t\t' + str(corp[2]) + '\n')
				else:
					for corp in self.corpus['_']:
						if corp[1] != file_in and tokenCompare(body, corp[0]):
							link_tuple = (lineNum, corp[1], corp[2])
							if link_tuple in link_tuples:
								continue
							else:
								link_tuples.append(link_tuple)
								if corp[1] in link_count.keys():
									link_count[corp[1]] += 1
								else:
									link_count[corp[1]] = 1
								lexi_out.write(lineNum + '\t\t' + corp[1] + '\t\t' + str(corp[2]) + '\n')

			if len(link_count.keys())==0:
				lexi_out.write('\n\nNo good links are found.')
			else:
				most_linked = max(link_count.iteritems(), key = operator.itemgetter(1))
				lexi_out.write('\n\nThe best linked code is %s, and %d links are found.' %most_linked)

			lexi_in.close()
			lexi_out.close()


		# lexi_inputs = self.getFiles('test_temp', 'lexi_results')
		# for lexi_input in lexi_inputs

	def getFiles(self, target):
		target_path = 'test_input/' + target
		target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
		if '.DS_Store' in target_files: 
			target_files.remove('.DS_Store')
		return target_files

	def biSearch(self, corp, val):
		left, right = 0, len(corp) - 1
		middle = -1
		while left<right:
			middle = (left + right)/2
			if corp[middle][0][0]< val[0]:
				left = middle + 1
			elif corp[middle][0][0]>val[0]:
				right = middle - 1
			else:
				return middle
			if right - left <=1:
				if corp[right][0][0] == val[0]:
					return right
				if corp[left][0][0] == val[0]:
					return left
				return -1


if __name__ == '__main__':
	folder = 'CodeJam/2A/python'
	# folder = 'sort_codes'
	buildinks = buildlinks(folder)