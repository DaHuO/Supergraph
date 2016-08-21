# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(1, T + 1):
    N = int(raw_input())
    s = set()
    for i in xrange(1, 10000):
        M = i * N
        for c in str(M):
            s.add(c)
        if len(s) == 10:
            break
    if len(s) == 10:
        print "Case #%d: %d" % (loop, M)
    else:
        print "Case #%d: INSOMNIA" % (loop)

