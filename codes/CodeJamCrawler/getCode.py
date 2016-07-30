#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import zipfile
import os

def downloadCode(input_file, target_folder):
	file_in = open(input_file, 'r')
	for link in file_in:
		name = link[link.rfind('=') + 1: -1]
		print name
		zipFile = urllib2.urlopen(link)
		with open(target_folder + name + '.zip', 'wb') as output:
			output.write(zipFile.read())
		zipobj = zipfile.ZipFile(target_folder + name + '.zip')
		zipobj.extractall(target_folder + name)
		os.remove(target_folder + name + '.zip')



if __name__ == "__main__":
	input_file = 'links.txt'
	target_folder = '2A/python/'
	downloadCode(input_file, target_folder)
