# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for loop in xrange(1, T + 1):
    S = list(raw_input())
    N = len(S)
    ans = 0
    for i in xrange(N - 1, -1, -1):
        if S[i] != "+":
            if i > 0 and S[0] != "-":
                for j in xrange(i):
                    if S[j] != "+": break
                    S[j] = "-"
                ans += 1
            S[:i + 1] = [S[j] for j in xrange(i, -1, -1)] 
            for j in xrange(i + 1):
                S[j] = "+" if S[j] == "-" else "-"
            ans += 1
    print "Case #%d: %d" % (loop, ans)
