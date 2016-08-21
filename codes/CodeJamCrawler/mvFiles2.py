#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile


def main(count, folders, target):
	for folder in folders:
		files = getFiles(folder)
		n = 0
		for f in files:
			path = folder + '/' + f
			copyfile(path, target + '/' + f)
			n += 1
			if n==count:
				break

def getFiles(folder):
	target_path = folder
	target_files = [f for f in listdir(target_path) if isfile(join(target_path, f))]
	if '.DS_Store' in target_files: 
		target_files.remove('.DS_Store')
	return target_files


if __name__ == '__main__':
	folders = ['16_0_1_neat','16_0_2_neat','16_0_3_neat','16_0_4_neat','16_1_1_neat','16_1_2_neat','16_2_1_neat','16_2_2_neat','16_3_1_neat']
	count = 490
	target = 'CJ'
	main(count, folders, target)