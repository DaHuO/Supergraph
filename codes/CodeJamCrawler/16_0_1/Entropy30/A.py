# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:36:24 2016

@author: dagoth
"""

import numpy as np
ms = [0] * 10

def mark(dig):
    s = str(dig)
    for i in range(len(s)):
        ms[int(s[i])] = 1
    if sum(ms) == 10:
        return 1
    else:
        return 0
                   
                   
                   
f = open('/home/dagoth/A-large.in', 'r')
f_w = open('/home/dagoth/A.out', 'w')
T = int(f.readline())
i = 1

for line in f.readlines():
    ms = [0] * 10
    N = int(line)
    
    if N == 0:
        f_w.write('Case #' + str(i) + ": " + 'INSOMNIA\n')
        
    cur = N
    for j in range(1000000):
        res = mark(cur)
        if res == 1:
            f_w.write('Case #' + str(i) + ": " + str(cur) + '\n')
            break
        cur += N
    i += 1