# -*- coding: utf-8 -*-
import sys
from collections import Counter, defaultdict
from itertools import cycle, chain, combinations

def letter_from_int(i):
    return chr(i+65)

def next_step(P):
    s = sum(p for (_,p) in P)
    P.sort(key=lambda (i,p):p, reverse=True)
    i,x = P[0]
    j,y = P[1]
    if x == y == 0:
        return None
    if (x-1) > (s-1)/2  or y > (s-1)/2 :
        P[0] = (i,x-1)
        P[1] = (j,y-1)
        return (i,j)
    P[0] = (i, x-1)
    return (i,)

filename = sys.argv[1]
with open(filename) as f:
    n_cases = int(f.readline())
    for i in xrange(n_cases):
        N = int(f.readline())
        P = list((i, int(p)) for (i,p) in enumerate(f.readline().strip().split()))
        sys.stdout.write('Case #{c}: '.format(c=i+1))
        while True:
            step = next_step(P)
            if step is None:
                break
            string = "".join(map(letter_from_int, step))
            sys.stdout.write(string+' ')
        print


        
