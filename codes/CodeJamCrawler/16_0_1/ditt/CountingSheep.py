# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:25:53 2016

@author: Dittaya Wanvarie
"""

def countingSheep(N):
    if N == 0:
        return 'INSOMNIA'
    
    digitSet = set()
    i = 1
    while len(digitSet) < 10:
        digits = i * N
        while digits > 0:
            digit = digits % 10
            digits //= 10
            
            digitSet.add(digit)
    
        i += 1
    return str((i-1)*N)

fout = open('A-large.out','w')
with open('A-large.in') as f:
    nCases = f.readline()
    case = 1
    for line in f:
        N = int(line)

        print('Case #'+str(case)+': '+countingSheep(N), file=fout)
        case += 1
fout.flush()
fout.close()