# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 01:54:52 2016

@author: Ghomam
"""
import sys
print sys.argv[1]
inp = open(sys.argv[1]).readlines()


def raw_input():
    return inp.pop(0).strip()

# Read input data
T = int(raw_input())
S = []
for i in xrange(T):
    S.append(raw_input())
    
O = [0 for s in S]
for i,s in enumerate(S):
    old = '+'
    x = 0
    for j in xrange(len(s)-1, -1, -1):
        if s[j] != old:
            old = s[j]
            x += 1
    O[i] = x
    



# output
output = open('output.out', 'w')
for i,o in enumerate(O):
    out = 'Case #{}: {}'.format(i+1, o)
    print out
    if i > 0 : out = '\n'+out
    output.write(out)
output.close()