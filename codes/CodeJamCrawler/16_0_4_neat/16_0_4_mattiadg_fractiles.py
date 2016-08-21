# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 11:29:09 2016

@author: mattia
"""
from numpy import ceil, arange

with open('D-small-attempt0.in', 'r') as fin, open('out.txt', 'w') as fout:
    T = int(fin.readline())
    for case in range(1, T+1):
        line = fin.readline().rstrip().split(" ")
        K, C, S = int(line[0]), int(line[1]), int(line[2])
        L = []
        if K == 1:
            fout.write('Case #' + str(case) + ": 1\n")
        elif C == 1:
            if K == S:
                L = arange(K) + 1
                fout.write('Case #' + str(case) + ": ")
                for l in L:
                    fout.write(str(l) + " ")
                fout.write('\n')
            else:
                fout.write('Case #' + str(case) + ": IMPOSSIBLE\n")
        elif S < ceil(K/2):
            fout.write('Case #' + str(case) + ": IMPOSSIBLE\n")
        else:
            for i in range(2, K+1, 2):
                L.append((i-1) * K**(C-1) + i - 1)
            if i < K:
                L.append((i-1) * K**(C-1) + i + 1)
            fout.write('Case #' + str(case) + ": ")
            for l in L:
                fout.write(str(l) + " ")
            fout.write('\n')