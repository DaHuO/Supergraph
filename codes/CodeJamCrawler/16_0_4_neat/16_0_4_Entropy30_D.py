# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:36:24 2016

@author: dagoth
"""

import numpy as np

                                      
f = open('/home/dagoth/D-small-attempt1.in', 'r')
f_w = open('/home/dagoth/D.out', 'w')
T = int(f.readline())

W = 1
for line in f.readlines():
    data = [int(p) for p in line.split()]
    K, C, S = data[0], data[1], data[2]
    
    if(C == 1):
        if(S < K):
            f_w.write('Case #' + str(W) + ': ' + 'IMPOSSIBLE' + '\n')
        else:
            f_w.write('Case #' + str(W) + ': ')
            for i in range(1, S + 1):
                f_w.write(str(i) + ' ')
            f_w.write('\n')
            
    elif(S < (K - 1)):
         f_w.write('Case #' + str(W) + ': ' + 'IMPOSSIBLE' + '\n')
    else:
        if K == 1:
            f_w.write('Case #' + str(W) + ': ' + str(1) + '\n')
        else:
            f_w.write('Case #' + str(W) + ': ')
            for i in range(2, S + 1):
                f_w.write(str(i) + ' ')
            f_w.write('\n')
        
    W += 1
    