#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import listdir
from os.path import isfile, join
import string

class Corpus(object):
	def __init__(self, input_folder):
		self.corpus = {}
		for lower in string.lowercase[:26]:
			self.corpus[lower] = []
		for upper in string.uppercase[:26]:
			self.corpus[upper] = []
		for i in range(10):
			self.corpus[str(i)] = []
		self.corpus['_'] = []
		input_files = self.getInput(input_folder)
		self.createCorpus(input_folder, input_files)

	def getInput(self, input_folder):
		path = 'test_temp/' + input_folder
		input_files = [f for f in listdir(path) if isfile(join(path, f))]
		return input_files

	def getCorpus(self):
		return self.corpus

	def createCorpus(self, input_folder, input_files):
		for File in input_files:
			file_in = "test_temp/" + input_folder + "/" + File
			f = open(file_in, 'r')
			for line in f:
				line = line.strip()
				flag = line.rfind('\t\t')
				body = line[:flag].split(' ')
				body.remove('')
				lineNum = int(line[flag+2:])
				for i in range(len(body) - 1):
					if body[i][0] in self.corpus.keys():
						length = len(self.corpus[body[i][0]])
						self.corpus[body[i][0]].append([body[i:], File[:-9], lineNum])
					else:
						self.corpus['_'].append([body[i:], File[:-9], lineNum])
			f.close()
		file_out = open('test_temp/corpus.txt','w')
		for key in self.corpus.keys():
			file_out.write('\n*****************************\n')
			file_out.write(str(self.corpus[key]))
		file_out.close()



if __name__ == '__main__':
	input_folder = 'lexi_results'
	corpus = Corpus(input_folder)