#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import zipfile
import os
import time

def downloadCode(input_file, target_folder):
	file_in = open(input_file, 'r')
	count = 0
	for link in file_in:
		name = link[link.rfind('=') + 1: -1]
		print name
		try:
			zipFile = urllib2.urlopen(link)
			with open(target_folder + name + '.zip', 'wb') as output:
				output.write(zipFile.read())
			zipobj = zipfile.ZipFile(target_folder + name + '.zip')
			zipobj.extractall(target_folder + name)
			os.remove(target_folder + name + '.zip')
			count += 1
		except Exception,e:
			print Exception,":",e
			continue
		print count



if __name__ == "__main__":
	input_file = 'links_16_4_3.txt'
	target_folder = '16_4_3/'
	if not os.path.exists(target_folder):
		os.makedirs(target_folder)
	start = time.time()
	downloadCode(input_file, target_folder)
	end = time.time()
	print end - start
