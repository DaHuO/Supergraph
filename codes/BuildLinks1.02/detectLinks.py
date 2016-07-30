#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import math

class detectLinks(object):
	def __init__(self, input_folder, codes, partialIndex, threshold, GTP):
		# self.input_codes = self.getInputCodes(input_folder)
		self.input_codes = codes
		self.partialIndex = partialIndex
		self.threshold = threshold
		# self.fout = open('temp.txt','w')
		self.GTP = GTP
		self.Candidates = self.getLinks(input_folder)
		# self.fout.close()


	def getInputCodes(self, input_folder):
		target_path = 'test_results' + input_folder[input_folder.find('/'):] + '/lexi_results'
		target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
		if '.DS_Store' in target_files: 
			target_files.remove('.DS_Store')
		# target_files_path = map(lambda x: target_path + '/' + x,target_files)
		codes = {}
		for f in target_files:
			path = target_path + '/' + f
			f_name = f[:f.rfind('_')]
			f = open(path, 'r')
			codes[f_name] = {}
			for line in f:
				flag = line.rfind('\t\t')
				data = line[:flag].split(' ')
				data.remove('')
				lineNum = int(line[flag+2:])
				codes[f_name][lineNum] = data
		# print codes
		return codes

	def getLinks(self, input_folder):
		outpathprefix = 'test_results' + input_folder[input_folder.find('/'):] + '/link_results/'
		for f in self.input_codes.keys():
			print f
			file_out = open(outpathprefix + f + '.txt', 'w')
			count = 0
			c_ = 0
			real_count = 0
			for lineNum in self.input_codes[f].keys():
				line = self.input_codes[f][lineNum]
				line.sort(key = lambda x: self.GTP.index(x))
				n = int(len(line) - math.ceil(len(line) * self.threshold) + 1)
				for i in range(n):
					t = line[i]
					for c in self.partialIndex[t]:
						if f == c[2]:
							continue
						if len(self.input_codes[c[2]][c[3]]) < int(self.threshold * len(line)):
							pass
						else:
							ct = int(math.ceil(max(len(line), len(self.input_codes[c[2]][c[3]])) * self.threshold))
							# print ct
							ubound = 1 + min(len(line) - i - 1, len(self.input_codes[c[2]][c[3]]) - c[1] - 1)
							if ubound >=ct:
								count += 1
								# print self.input_codes[c[2]][c[3]]
								target = self.input_codes[c[2]][c[3]]
								# target.sort(key = lambda x: self.GTP.index(x))
								# print target
								if self.verifyLink(line, target, ct):
									# print 'got link!'
									real_count += 1
									file_out.write(str(lineNum)+'\t\t'+c[2]+'\t\t'+str(c[3])+'\n')
							else:
								c_ += 1
			# print f
			# print real_count
			# print 'count,' ,count
			file_out.close()

	def verifyLink(self, line1, line2, ct):
		# self.fout.write(str(line1) + ' '+ str(line2) + ' ' + str(ct) + ' ')
		# print line1, line2, ct
		count = 0
		p1 = 0
		p2 = 0
		while p1 < len(line1) and p2 < len(line2):
			if count >= ct:
				break
			if line1[p1] == line2[p2]:
				count += 1
			if self.GTP.index(line1[p1])<self.GTP.index(line2[p2]):
				p1 += 1
			else:
				p2 += 1
		if count>=ct:
			# self.fout.write('True\n')
			return True
		else:
			# self.fout.write('False\n')
			return False







