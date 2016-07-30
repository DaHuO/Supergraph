#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from shutil import copyfile

for directory in os.listdir("python"):
	prefix = directory
	for file in os.listdir("python/" + directory):
		copyfile("python/" + directory + '/' + file, 'python_neat/' + prefix + '_' + file)