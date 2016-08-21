#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isfile, join


def check(folder):
	count = {}
	count['1'] = [0,0,0,0,0,0]    #in order: directlink1, directlink2, directlink3
	count['2'] = [0,0,0,0,0,0]    #sametokenlink1, sametokenlink2,sametokenlink3
	count['3'] = [0,0,0,0,0,0]
	files = getFiles(folder)
	for f in files:
		target = f[5]
		fin = open(folder + '/' + f, 'r')
		flag = True
		drecord = []
		trecord = []
		for line in fin:
			line = line.strip()
			if len(line)==0:
				continue
			if line[:6] == 'Direct':
				flag = True
				continue
			if line[:4] == 'With':
				flag = False
				continue
			if line[-1] == ':':
				continue
			if flag:
				if line in drecord:
					continue
				else:
					drecord.append(line)
					part = line.split('\t:\t')
					prob = int(part[0][5])
					count[target][prob-1] += 1
			else:
				if line in trecord:
					continue
				else:
					trecord.append(line)
					part = line.split('\t:\t')
					prob = int(part[0][5])
					count[target][2+prob] += 1
		fin.close()
	print count



def getFiles(folder):
	target_path = folder
	target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
	if '.DS_Store' in target_files: 
		target_files.remove('.DS_Store')
	return target_files


if __name__ == '__main__':
	folder = 'test_results/CJ_16_1/link_results'
	check(folder)