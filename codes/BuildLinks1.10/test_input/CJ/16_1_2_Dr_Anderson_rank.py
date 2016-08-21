# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

#1
#3
#1 2 3
#2 3 5
#3 5 6
#2 3 4
#1 2 3

import numpy as np

T = int(raw_input())
for i in xrange(1, T + 1):
	N = int(raw_input())
	rank = []*0
	for n in range(2*N-1):
		rank = rank + [int(s) for s in raw_input().split(" ")]
	
	rank.sort()
	hOut = []*0
	
	currH = rank[0]
	count = 1
	for n in xrange(len(rank)-1):
		if rank[n+1] == currH:
			count = count + 1
		else:
			if count % 2 == 1:
				hOut = hOut + [currH]

			currH = rank[n+1]
			count = 1
	
	if count % 2 == 1:
		hOut = hOut + [currH]
			
	hOut.sort()

	print "Case #{}: {}".format(i, " ".join(map(str,hOut)))