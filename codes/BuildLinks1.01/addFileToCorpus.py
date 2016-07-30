#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lexicalAnalysis import lexicalanalysis
from tokenCompare import tokenCompare

import sys
import string
import operator


def addFileToCorpus(file_in, target_corpus):
	temp = lexicalanalysis(target_corpus[(len('test_temp/')):-len('/corpus.txt')], file_in, True)
	newCorpus = readCorpusFile(target_corpus)
	f = open(target_corpus[:-len('corpus.txt')] + 'lexi_results/' + file_in[:file_in.rfind('.')] + '_lexi.txt', 'r')
	for line in f:
		line = line.strip()
		if len(line)==0:
			continue
		flag = line.rfind('\t\t')
		body = line[:flag].split(' ')
		body = [value for value in body if value != '']
		lineNum = int(line[flag+2:])
		for i in range(len(body) - 1):
			if body[i][0] in newCorpus.keys():
				newCorpus[body[i][0]].append([body[i:], file_in[:file_in.rfind('.')], lineNum])
			else:
				newCorpus['_'].append([body[i:], file_in[:file_in.rfind('.')], lineNum])
	f.close()
	file_out = open(target_corpus, 'w')
	for key in newCorpus.keys():
		file_out.write('\n*****************************\n')
		for element in newCorpus[key]:
			out = ''
			for el in element[0]:
				out = out + el + '\t\t\t'
			file_out.write(out + '\t' + element[1] + '\t\t\t\t' + str(element[2]) + '\n')
	file_out.close()

	return newCorpus
	
def getLinkResult(file_in, newCorpus):
	lexi_in = open(target_corpus[:-len('corpus.txt')] + 'lexi_results/' + file_in[:file_in.rfind('.')] + '_lexi.txt', 'r')
	lexi_out = open(target_corpus[:-len('corpus.txt')] + 'link_results/' + file_in[:file_in.rfind('.')] + '_link.txt', 'w')
	link_count = {}
	link_tuples = []
	lines = []
	for line in lexi_in:
		print line
		line = line.strip()
		flag = line.rfind('\t\t')
		body = line[:flag].split(' ')
		if len(body)<=1:
			continue
		if body in lines:
			continue
		lineNum = line[flag+2:]
		if body[0][0] in newCorpus.keys():
			for corp in newCorpus[body[0][0]]:
				if corp[1] != file_in and tokenCompare(body, corp[0]) :
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
		else:
			for corp in newCorpus['_']:
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


def readCorpusFile(target_corpus):
	corpus_file = open(target_corpus, 'r')

	corpus = {}
	for lower in string.lowercase[:26]:
		corpus[lower] = []
	for upper in string.uppercase[:26]:
		corpus[upper] = []
	for i in range(10):
		corpus[str(i)] = []
	corpus['_'] = []
	for line in corpus_file:
		line = line.strip()
		if len(line)==0:
			continue
		if line[0] == '*':
			continue
		data_set = line.split('\t\t\t\t')
		tokens = data_set[0].split('\t\t\t')
		el = [tokens, data_set[1], int(data_set[2])]
		if tokens[0][0] in corpus.keys():
			corpus[tokens[0][0]].append(el)
		else:
			corpus['_'].append(el)
	corpus_file.close()
	return corpus


if __name__ == '__main__':
	if len(sys.argv)!=3:
		print "please add arguments as [input file] [corpus location]"
	else:
		file_in = sys.argv[1]
		target_corpus = sys.argv[2]
		newCorpus = addFileToCorpus(file_in, target_corpus)
		getLinkResult(file_in, newCorpus)