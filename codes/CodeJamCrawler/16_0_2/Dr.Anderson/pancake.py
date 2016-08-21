# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

import numpy as np
from util import replace

N = int(raw_input())
for i in xrange(1, N + 1):
	pan = list(raw_input())
	replace(pan, '-', 0)
	replace(pan, '+', 1)
	x = np.sum(np.abs(np.diff(np.array(pan))))
	x = x + 1 - pan[-1]
	
	print "Case #{}: {}".format(i, x)