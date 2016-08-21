# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:36:24 2016

@author: dagoth
"""

import numpy as np

def flip(seq, d):
    ss = seq[:(d + 1)]
    ss = ss[::-1]
    new_s = ''
    for i in range(len(ss)):
        if ss[i] == '+':
            new_s = new_s + '-'
        else:
            new_s = new_s + '+'
    new_s += seq[(d + 1):]
    return new_s
    
f = open('/home/dagoth/B-large.in', 'r')
f_w = open('/home/dagoth/B_res.txt', 'w')
W = 1
T = int(f.readline())
for line in f.readlines():
    s = line
    turns = 0

    for q in range(len(s) - 1, -1, -1):
        if s[q] == '-':
            if s[0] == '-':
                turns += 1
                s = flip(s, q)
            else:
                for j in range(q - 1, -1, -1):
                    if s[j] == '+':
                       s = flip(s, j)
                       s = flip(s, q)
                       turns += 2
                       break
    print(turns)
    f_w.write('Case #' + str(W) + ': ' + str(turns) + '\n')
    W = W + 1
                   