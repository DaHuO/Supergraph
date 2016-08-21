# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:29:57 2015

@author: vbd
"""

inp = raw_input()
T = int(inp)

for c in range(1,T+1) :
    inp = raw_input()
    S = inp.strip()

    top = S[0]
    bottom = S[-1]
    flips = 0
    prev = top
    for p in S:
        if p != prev:
            flips += 1
            prev = p
    if bottom == '-':
        flips += 1
    print "Case #{0}: {1}".format(c,flips)
