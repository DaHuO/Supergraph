#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import listdir
from os.path import isfile, join
import string
import bisect

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
		# print input_files
		for f in input_files:
			if f == '.DS_Store':
				input_files.remove(f)
		return input_files

	def getCorpus(self):
		return self.corpus

	def createCorpus(self, input_folder, input_files):
		prefix_record = {}
		for lower in string.lowercase[:26]:
			prefix_record[lower] = []
		for upper in string.uppercase[:26]:
			prefix_record[upper] = []
		for i in range(10):
			prefix_record[str(i)] = []
		prefix_record['_'] = []


		for File in input_files:
			# print File
			file_in = "test_temp/" + input_folder + "/" + File
			f = open(file_in, 'r')
			for line in f:
				line = line.strip()
				if len(line)==0:
					continue
				flag = line.rfind('\t\t')
				body = line[:flag].split(' ')
				body = [value for value in body if value != '']
				lineNum = int(line[flag+2:])
				# print body
				for i in range(len(body) - 1):
					toInsert = [body[i:], File[:-9], lineNum]
					if body[i][0] in self.corpus.keys():
						pos = bisect.bisect(prefix_record[body[i][0]], body[i])
						bisect.insort(prefix_record[body[i][0]], body[i])
						# self.biInsert(self.corpus[body[i][0]], toInsert)
						self.corpus[body[i][0]].insert(pos, toInsert)
						# self.corpus[body[i][0]].append([body[i:], File[:-9], lineNum])
						# self.corpus[body[i][0]] = sorted(self.corpus[body[i][0]], key=lambda ele: ele[0][0])
					else:
						# self.corpus['_'].append([body[i:], File[:-9], lineNum])
						# self.corpus['_'] = sorted(self.corpus['_'], key=lambda ele: ele[0][0])
						# self.biInsert(self.corpus['_'], toInsert)
						pos = bisect.bisect(prefix_record['_'], body[i])
						bisect.insort(prefix_record['_'], body[i])
						self.corpus['_'].insert(pos, toInsert)
			f.close()
		# print self.corpus
		file_out = open('test_temp/' + input_folder[:-len('/lexi_results')] + '/corpus.txt','w')
		for key in self.corpus.keys():
			file_out.write('\n*****************************\n')
			for element in self.corpus[key]:
				out = ''
				for el in element[0]:
					out = out + el + '\t\t\t'
				file_out.write(out + '\t' + element[1] + '\t\t\t\t' + str(element[2]) + '\n')
			# file_out.write(str(self.corpus[key]))
		print len(self.corpus)
		file_out.close()

	def biInsert(self, target, val):
		temp = []
		for corp in target:
			temp.append(corp[0][0])
		flag = bisect.bisect(temp, val[0][0])
		target.insert(flag, val)
		# if len(target) == 0:
		# 	target.append(val)
		# 	return
		# left, right = 0, len(target)-1
		# middle = left
		# while left<=right:
		# 	middle = (left + right)/2
		# 	if target[middle][0][0] < val[0][0]:
		# 		left = middle + 1
		# 	else:
		# 		right = middle - 1
		# 	if left == len(target):
		# 		middle = len(target)
		# 		break
		# 	if right == -1:
		# 		middle = 0
		# 		break
		# 	if target[left][0][0] == target[right][0][0]:
		# 		break
		# 	if left == right-1:
		# 		middle = right
		# 		break
		# target.insert(middle, val)




if __name__ == '__main__':
	input_folder = 'lexi_results'
	corpus = Corpus(input_folder)