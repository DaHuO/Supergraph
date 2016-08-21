# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:29:57 2015

@author: vbd
"""

def find_max_prod(n):
    digits = []
    for d in str(n):
        if d not in digits:
            digits.append(d)
    i = 2
    while len(digits) < 10:
        for d in str(i*n):
            if d not in digits:
                digits.append(d)
        i += 1
    return (i-1)*n

inp = raw_input()
T = int(inp)

for c in range(1,T+1) :
    inp = raw_input()
    N = int(inp)

    if N == 0:
        y = "INSOMNIA"
    else:
        y = find_max_prod(N)
    print "Case #{0}: {1}".format(c,y)
