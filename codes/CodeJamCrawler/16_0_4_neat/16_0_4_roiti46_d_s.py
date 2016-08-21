# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(1, T + 1):
    K, C, S = map(int, raw_input().split())
    if K == 1:
        ans = [1]
    elif C == 1:
        ans = range(1, S + 1)
    else:
        ans = [2 + K**(C - 1)*i for i in xrange(S)]

    print "Case #%d:" % loop, " ".join(map(str, ans))
