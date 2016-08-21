# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

#WRWWLWWLWWLWLWRRWRWWWRWWRWLW WWRRWLWLWWLWWLWWRWWRWWLW

import numpy as np

N = int(raw_input())
for i in xrange(1, N + 1):
	K, C, S = [int(s) for s in raw_input().split(" ")]
	print "Case #{}: {}".format(i, ' '.join(map(str,np.array(xrange(1,S+1)))))
