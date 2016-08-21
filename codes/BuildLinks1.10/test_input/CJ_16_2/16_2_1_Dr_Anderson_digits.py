# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

import numpy as np
from util import replace

def remove(S, idx):
	Sout = S[:idx]+S[idx+1:]
	return Sout

def removenum(S, num):
	for n in range(len(num)):
		S = remove(S,S.index(num[n]))
	
	return S

T = int(raw_input())
for i in xrange(1, T + 1):
	S = raw_input().strip()
	out = []*0
	
	# Strip evens first
	hitflag = 1
	while(hitflag == 1):
		hitflag = 0
		idx = S.find('Z')
		if(idx > -1):
			hitflag = 1
			out = out + [0]
			S = removenum(S, 'ZERO');
		idx = S.find('W')
		if(idx > -1):
			hitflag = 1
			out = out + [2]
			S = removenum(S, 'TWO');
		idx = S.find('U')
		if(idx > -1):
			hitflag = 1
			out = out + [4]
			S = removenum(S, 'FOUR');
		idx = S.find('X')
		if(idx > -1):
			hitflag = 1
			out = out + [6]
			S = removenum(S, 'SIX');
		idx = S.find('G')
		if(idx > -1):
			hitflag = 1
			out = out + [8]
			S = removenum(S, 'EIGHT');

	# Strip some odds
	hitflag = 1
	while(hitflag == 1):
		hitflag = 0
		idx = S.find('O')
		if(idx > -1):
			hitflag = 1
			out = out + [1]
			S = removenum(S, 'ONE');
		idx = S.find('T')
		if(idx > -1):
			hitflag = 1
			out = out + [3]
			S = removenum(S, 'THREE');
		idx = S.find('F')
		if(idx > -1):
			hitflag = 1
			out = out + [5]
			S = removenum(S, 'FIVE');

	hitflag = 1
	while(hitflag == 1):
		hitflag = 0
		idx = S.find('V')
		if(idx > -1):
			hitflag = 1
			out = out + [7]
			S = removenum(S, 'SEVEN');
		idx = S.find('I')
		if(idx > -1):
			hitflag = 1
			out = out + [9]
			S = removenum(S, 'NINE');

	out.sort()
			
	print "Case #{}: {}".format(i, "".join(map(str,out)))