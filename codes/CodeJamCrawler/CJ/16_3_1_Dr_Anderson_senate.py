# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

#WRWWLWWLWWLWLWRRWRWWWRWWRWLW WWRRWLWLWWLWWLWWRWWRWWLW

import numpy as np

T = int(raw_input())
for i in xrange(1, T + 1):
	N = int(raw_input())
	P = [int(_) for _ in raw_input().split(" ")]
	evac = ' '
	while sum(P) != 0:
		mp = max(P)
		mpidx = P.index(mp)
		P[mpidx] = P[mpidx]-1
		if sum(P) - max(P) >= max(P):
			evac = evac +  ' ' + chr(mpidx + ord('A'))
		else:
			mp2 = max(P)
			mpidx2 = P.index(mp2)
			evac = evac + ' ' + chr(mpidx + ord('A')) + chr(mpidx2 + ord('A'))
			P[mpidx2] = P[mpidx2]-1
			
	print "Case #{}: {}".format(i,evac)