# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

#WRWWLWWLWWLWLWRRWRWWWRWWRWLW WWRRWLWLWWLWWLWWRWWRWWLW

import numpy as np
#5
#0
#1
#2
#11
#1692

def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))

N = int(raw_input())
for i in xrange(1, N + 1):
	num = int(raw_input())
	sheep = list(str(num))
	insom = True
	for n in xrange(1,10000):
		
		sheep = union(sheep,list(str(num*n)))
		if len(sheep) == 10:
			print "Case #{}: {}".format(i, n*num)
			insom = False
			break
	if insom:
		print "Case #{}: {}".format(i, 'INSOMNIA')
