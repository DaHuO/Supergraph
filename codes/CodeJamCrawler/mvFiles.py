#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from shutil import copyfile
from os import listdir
from os.path import isfile, join

def main(file_prefix, count):
	target = 'CJ_' + file_prefix
	if not os.path.exists(target):
		os.makedirs(target)
	for i in range(1, count + 1):
		folder_path = file_prefix + '_' + str(i) + '_neat/'
		print folder_path
		files = getFiles(folder_path)
		for f in files:
			path = folder_path + f
			copyfile(path, target + '/' + f)

def getFiles(folder):
	target_path = folder
	target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
	if '.DS_Store' in target_files: 
		target_files.remove('.DS_Store')
	return target_files

if __name__ == '__main__':
	file_prefix = '16_2'
	count = 3
	main(file_prefix, count)