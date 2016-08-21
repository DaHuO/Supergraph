#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from shutil import copyfile

folder = '16_4_3'
target_folder = folder + '_neat'
if not os.path.exists(target_folder):
	os.makedirs(target_folder)
count = 0
countf = 0
for directory in os.listdir(folder):
	count += 1
	prefix = folder + '_' + directory
	if directory == '.DS_Store':
		continue
	while '.' in prefix:
		prefix = prefix.replace('.','_')
		print prefix
	for file in os.listdir(folder + '/' + directory):
		if file[-3:] != '.py':
			print 'not a python file'
			continue
		copyfile(folder + "/" + directory + '/' + file, target_folder + '/' + prefix + '_' + file)
		countf += 1
print count
print countf