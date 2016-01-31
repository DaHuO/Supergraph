#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
class HuffmanString:

	def __init__(self, File, mode):
		self.File = File
		self.mode = mode
		self.encode_result = self.parse(mode)

	def get_encode_result(self):
		return self.encode_result

	def FirstRun(self, mode):
		StringRecord = {}
		for line in self.File:
			line = line.strip()
			if len(line) == 0:
				continue
			if mode == "line":
				if line in StringRecord:
					StringRecord[line] += 1
				else:
					StringRecord[line] = 1
			elif mode == "word":
				line = line.split(' ')
				for word in line:
					word = word.strip()
					if len(word) == 0:
						continue
					if word in StringRecord:
						StringRecord[word] += 1
					else:
						StringRecord[word] = 1
		return StringRecord

	def printRecord(self, SortedStringRecord, StringRecord):
		for string in SortedStringRecord:
			print string + str(StringRecord[string])

	def sort(self, StringRecord):
		SortedStringRecord = sorted(StringRecord, key = StringRecord.get, reverse = False)
		return SortedStringRecord

	def encode(self,SortedStringRecord, StringRecord):
		listOfNode = []
		for string in SortedStringRecord:
			listOfNode.append(Node(weight = StringRecord[string], string = string))
		ListOfNode = self.Huffman(listOfNode)
		encodeDict = {}
		for e in listOfNode:
			ep = e
			encodeDict[e.string] = ""
			while ep != ListOfNode[0]:
				if ep.parent.left == ep:
					encodeDict[e.string] += "1"
				else:
					encodeDict[e.string] += "0"
				ep = ep.parent
		return encodeDict

	def Huffman(self, listOfNode):
		listOfNode = list(listOfNode)
		while len(listOfNode) != 1:
			a,b = listOfNode[0], listOfNode[1]
			new = Node()
			new.weight, new.left, new.right = a.weight + b.weight, a, b
			a.parent = new
			b.parent = new
			listOfNode.remove(a)
			listOfNode.remove(b)
			listOfNode.append(new)
			listOfNode = sorted(listOfNode, key = lambda node:node.weight)
		return listOfNode

	def parse(self, mode):
		StringRecord = self.FirstRun(mode)
		SortedStringRecord = self.sort(StringRecord)
		return self.encode(SortedStringRecord, StringRecord)

class Node:
	def __init__(self,right=None,left=None,parent=None,weight=0,string=None):
		self.right = right
		self.left = left
		self.parent = parent
		self.weight = weight
		self.string = string

File_IN = open('test_codes/GoHttp.c','r')
File_OUT = open('test_results/GoHttp.txt', 'w')
input_arg = sys.argv

if len(input_arg)>2 or (input_arg[1]!='line' and input_arg[1]!='word'):
	print "input argument not right, take 'line' by default"
	input_arg[0] = 'line'
test = HuffmanString(File_IN, input_arg[1])
encode_result = test.get_encode_result()
for e in encode_result:
	string = e + "\t:\t" + encode_result[e] + "\n"
	File_OUT.write(string)