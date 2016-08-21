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

def binToLG(state):
    return "".join([ 'L' if st == '0' else 'G' for st in state])

# Read input data
T = int(raw_input())
tests = []
for i in xrange(T):
    K, C, S = [int(n) for n in raw_input().split(" ")]
    tests.append([K,C,S])
    if K != S:
        print i+1, K, S


O = ['' for s in tests]
for i,(K,C,S) in enumerate(tests):
    O[i] =  [ str(s+1) for s in xrange(S)]


# output
output = open('output.out', 'w')
for i,o in enumerate(O):
    out = 'Case #{}: {}'.format(i+1, " ".join(list(o) ))
    print out
    if i > 0 : out = '\n'+out
    output.write(out)
output.close()