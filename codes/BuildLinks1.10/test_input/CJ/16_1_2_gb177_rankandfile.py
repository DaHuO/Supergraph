#!/usr/bin/python

import sys

from itertools import combinations

def Ni(): return tuple(map(int, sys.stdin.readline().split()))
def Nil(): return map(int, sys.stdin.readline().split())
def Ns(): return tuple(sys.stdin.readline().split())

T = Ni()[0]

# brute force 19 choose 10 ~ 92,000
for c in range(1, T+1):
    N = Ni()[0]
    lines = [Ni() for i in range(2*N-1)]
    lset = dict((v, k) for k, v in enumerate(lines))

    for cc in combinations(range(2*N-1), N):
         rows = [lines[i] for i in cc]
         rows.sort()
         cand = None
         for i in range(N):
            vert = tuple([rows[j][i] for j in range(N)])
            if vert in lset and lset[vert] not in cc:
                pass
            else:
                if cand:
                    cand = None
                    break
                else:
                    cand = vert
                    
         if cand:
             r = cand
             break

    print "Case #%d: %s" % (c, " ".join(map(str, r)))

