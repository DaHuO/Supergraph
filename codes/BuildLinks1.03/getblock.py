#!/usr/bin/env python
# -*- coding: utf-8 -*-

def blockdetect(fcode):
	tab = ''
	tabLength = 0
	fcode = open(fcode, 'r')
	for line in fcode:
		print line
		if line[0] == '\t':
			tab = '\t'
			tabLength = 1
			break
		if line[:2] == '  ' and line[2]!=' ':
			tab = '  '
			tabLength = 2
			break
		if line[:4] == '    ' and line[4]!= ' ':
			tab = '    '
			tabLength = 4
			break
	print 'tab is:%s' % (tab,)
	print tabLength

	lineNum = 1
	for line in fcode:
		if line[:tabLength] == tab:
			print 'hi there'


if __name__ == '__main__':
	# fin = 'test_input/CodeJam/2A/python/AdGold_A.py'
	fin = 'test.py'
	blockdetect(fin)