# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 01:38:46 2016

@author: Ghomam
"""
import sys

print sys.argv[1]
inp = open(sys.argv[1]).readlines()


def raw_input():
    return inp.pop(0)

# Read input data
T = int(raw_input())
N = []
for i in xrange(T):
    N.append(int(raw_input()))
    
O = [n for n in N]
for i,n in enumerate(N):
    out = []
    if n == 0:
        O[i] = 'INSOMNIA'
        continue
    for j in xrange(1, 100):
        num = str(j*n)
        for c in num:
            if c not in out:
                out.append(c)
        if len(out) == 10:
            break
    else:
        O[i] = 'INSOMNIA'
        continue
    O[i] = j*n

# output
output = open('output.out', 'w')
for i,o in enumerate(O):
    out = 'Case #{}: {}'.format(i+1, o)
    print out
    if i > 0 : out = '\n'+out
    output.write(out)
output.close()