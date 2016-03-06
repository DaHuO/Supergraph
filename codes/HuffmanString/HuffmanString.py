#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import file_search
import strFilter


class HuffmanString:
    def __init__(self, File_paths, mode, language, comment):
        self.File_paths = File_paths
        self.mode = mode
        self.language = language
        self.comment = comment
        self.encode_result = self.parse(mode)

    def get_encode_result(self):
        return self.encode_result

    def FirstRun(self, mode):
        StringRecord = {}
        count = 0
        for File in self.File_paths:
            file_in = open(File, 'r')

            for line in file_in:
                count += 1
                line = line.strip()
                if len(line) == 0:
                    continue
                if self.comment:
                    pass
                else:
                    if(line[0:2]=='//'):
                        continue
                if mode == "line":
                    if line in StringRecord:
                        StringRecord[line] += 1
                    else:
                        StringRecord[line] = 1
                elif mode == "word":
                    line = re.split('#|%|&|!|\(|\)|{|}|,|\.|\+|=|-|:|\\\|\/|\*|"|\'|;|\[|\]|<|>|\s*', line)
                    for word in line:
                        word = word.strip()
                        if len(word) == 0:
                            continue
                        if word in StringRecord:
                            StringRecord[word] += 1
                        else:
                            StringRecord[word] = 1
            file_in.close()
        return StringRecord

    def sort(self, StringRecord):
        SortedStringRecord = sorted(StringRecord, key=StringRecord.get, reverse=False)
        return SortedStringRecord

    def encode(self, SortedStringRecord, StringRecord):
        listOfNode = []
        for val in SortedStringRecord:
            listOfNode.append(Node(weight=StringRecord[val], string=val))
        ListOfNode = self.Huffman(listOfNode)
        encodeDict = []

        for e in listOfNode:
            if strFilter.filter(e.string, self.language):
                continue
            else:
                encodeDict.append([e.string, StringRecord[e.string]])
        encodeDict = reversed(encodeDict)

        return encodeDict


    def Huffman(self, listOfNode):
        listOfNode = list(listOfNode)
        while len(listOfNode) != 1:
            a, b = listOfNode[0], listOfNode[1]
            new = Node()
            new.weight, new.left, new.right = a.weight + b.weight, a, b
            a.parent = new
            b.parent = new
            listOfNode.remove(a)
            listOfNode.remove(b)
            listOfNode.append(new)
            listOfNode = sorted(listOfNode, key=lambda node: node.weight)
        return listOfNode

    def parse(self, mode):
        StringRecord = self.FirstRun(mode)
        SortedStringRecord = self.sort(StringRecord)
        return self.encode(SortedStringRecord, StringRecord)


class Node:
    def __init__(self, right=None, left=None, parent=None, weight=0, string=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.weight = weight
        self.string = string


input_arg = sys.argv
# File_IN = open('test_codes/httpd.c', 'r')

# if len(input_arg) > 2 or (input_arg[1] != 'line' and input_arg[1] != 'word'):
#     print "input argument not right, take 'line' by default"
#     input_arg[1] = 'line'

# File_OUT = open('test_results/httpd' + '_' + input_arg[1] + '.txt', 'w')
# test = HuffmanString(File_IN, input_arg[1])
# encode_result = test.get_encode_result()

# for e in encode_result:
#     # string = e + "\t:\t" + str(encode_result[e]) + "\n"
#     string = str(e) + '\n'
#     File_OUT.write(string)

path = input_arg[1]
mode = input_arg[2]
if input_arg[3]:
    language = input_arg[3]
else:
    language = ""
if input_arg[4] == '-c':
    comment = True
else:
    comment = False
file_paths = file_search.gci(path)
test = HuffmanString(file_paths, mode, language, comment)
encode_result = test.get_encode_result()
project_name = path[path.find('/'):]
if project_name.find('.')!=-1:
    project_name = project_name[:project_name.find('.')]
File_OUT = open('test_results/' + project_name + '_' + mode + '.txt', 'w')
for e in encode_result:
    string = str(e) + '\n'
    File_OUT.write(string)
File_OUT.close()

