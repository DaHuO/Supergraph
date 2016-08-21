#!/usr/bin/env python
# encoding: utf-8

"""
Submission for problem B: Revenge of the Pancakes
of Google CodeJam 2016

Author: Tsirigotis Christos <tsirif@gmail.com>
Date: April 09, 2016
"""


OUTPUT = "Case #%(nc)s: %(L)s"

def solve():
    T = int(raw_input()) # 1 <= T <= 100
    for nc in xrange(1, T+1):
        N = map(lambda x: 1 if x == '+' else 0, raw_input())
        S = len(N) # 1 <= S <= 10 <= 100
        L = 0
        ls = N[0]
        for i in xrange(1, S):
            if N[i] != ls:
                L += 1
                ls = N[i]
        if ls == 0:
            L += 1
        print(OUTPUT % locals())

solve()

