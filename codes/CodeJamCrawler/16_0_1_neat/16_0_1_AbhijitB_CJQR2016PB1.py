# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:23:31 2016

@author: abhibhat
"""

def CJQR2016PB1(N):
    from itertools import count
    seen = dict.fromkeys(map(str,range(10)))
    if N == 0: return "INSOMNIA"
    for i in count(1):
        for digit in str(N*i):
            seen[digit] = 0
        if None not in seen.values(): return N * i
T = input()
for i in range(1, T+1):
    print "Case #{}: {}".format(i, CJQR2016PB1(input()))