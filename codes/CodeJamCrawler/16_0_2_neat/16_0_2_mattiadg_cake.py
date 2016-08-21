# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:21:27 2016

@author: mattia

Ruotare una pila di pancakes per averli tutti rivolti con la faccia +
verso l'alto
"""            

with open('B-large.in', 'r') as fin, open('out.txt', 'w') as fout:
    T = int(fin.readline())
    for case in range(1, T+1):
        S = fin.readline().rstrip()
        count = 0        
        if S[0] == '-':
            count += 1
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                continue
            elif S[i] == '-':
                count += 2

        fout.write('Case #' + str(case) + ": " + str(count) + '\n')