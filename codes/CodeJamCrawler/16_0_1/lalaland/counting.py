# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:33:17 2016

@author: avishay
"""

import numpy as np
import re
import time

def solve(lines):
    N = int(lines[0])
    if N == 0: return 'INSOMNIA'
    seen = set()
    i = 0
    while len(seen) < 10:
        i += N
        tmp = i
        while tmp > 0:
            seen.add(tmp % 10)
            tmp //= 10
    return str(i)

lines = open('/home/avishay/Downloads/cj/counting/A-large.in').readlines()
num_cases = int(lines[0])
lines_per_case = 1
start = time.time()
o = open('/home/avishay/Downloads/cj/counting/large-out', 'w')
for i in range(num_cases):
    res = solve(lines[i*lines_per_case+1:(i+1)*lines_per_case+1])
    print('Case #%d: %s' % (i+1, res))
    o.write('Case #%d: %s\n' % (i+1, res))

o.close()
print('runtime=%.2f' % (time.time() - start))