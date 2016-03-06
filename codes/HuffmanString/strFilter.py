#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def filter(token, language):
	# match any real numbers
	if re.match(r'^[-+]?\d+(\.\d+)?$', token):
		return True
	# match hex or oct numbers
	if re.match(r'^0[xX]?\d*', token):
		return True

	if language.lower() == 'c':
		c_keywords = {'auto', 'break', 'case', 'char', 'const',
		'continue', 'default', 'do', 'double', 'else', 'enum',
		'extern', 'float', 'for', 'goto', 'if', 'int', 'long',
		'register', 'return', 'short', 'signed', 'sizeof', 'static',
		'struct', 'switch', 'typedef', 'union', 'unsigned', 
		'void', 'volatile', 'while'}
		if token in c_keywords:
			return True
	return False


