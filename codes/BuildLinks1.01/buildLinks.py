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


class buildlinks(object):
	def __init__(self, target):
		self.lexiAnalysis(target)
		self.corpus = self.createCorpus()
		print sys.getsizeof(self.corpus)
		mem = 0
		for key in self.corpus.keys():
			mem += sys.getsizeof(self.corpus[key])
		print mem
		self.buildLinks(target)

	def lexiAnalysis(self, target):
		target_files = self.getFiles(target)
		for target_file in target_files:
			temp = lexicalanalysis(target, target_file)

	def createCorpus(self):
		corpus = Corpus('lexi_results').getCorpus()
		return corpus

	def buildLinks(self, target):
		files = self.getFiles(target)
		keys = self.corpus.keys()
		# files_in = map(lambda x: x[:-3] + '_lexi.txt', files)
		for file_in in files:
			file_in = file_in[:-3]
			link_count = {}
			print file_in
			file_path = 'test_temp/lexi_results/' + file_in + '_lexi.txt'
			lexi_in = open(file_path, 'r')
			lexi_out = open('test_temp/link_results/' + file_in + '_link.txt', 'w')
			for line in lexi_in:
				line = line.strip()
				flag = line.rfind('\t\t')
				body = line[:flag].split(' ')
				body.remove('')
				lineNum = line[flag+2:]
				if body[0][0] in keys:
					for corp in self.corpus[body[0][0]]:
						if corp[1] != file_in and tokenCompare(body, corp[0]):
							if corp[1] in link_count.keys():
								link_count[corp[1]] += 1
							else:
								link_count[corp[1]] = 1
							lexi_out.write(lineNum + '\t\t' + corp[1] + '\t\t' + str(corp[2]) + '\n')
				else:
					for corp in self.corpus['_']:
						if corp[1] != file_in and tokenCompare(body, corp[0]):
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
		return target_files
		




if __name__ == '__main__':
	folder = 'sort_codes'
	buildinks = buildlinks(folder)