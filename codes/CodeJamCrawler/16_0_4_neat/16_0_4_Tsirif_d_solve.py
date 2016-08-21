#!/usr/bin/env python
# encoding: utf-8

"""
Submission for problem D: Fractiles
of Google CodeJam 2016

Author: Tsirigotis Christos <tsirif@gmail.com>
Date: April 09, 2016
"""

from collections import defaultdict

OUTPUT = "Case #%(nc)s:"
def print_output(output, L):
    for l in L:
        output += " "+str(l)
    print(output)

IMP = "IMPOSSIBLE"

def solve():
    T = int(raw_input()) # 1 <= T <= 100
    for nc in xrange(1, T+1):
        K, C, S = map(int, raw_input().split()) # 1<=K,C<=100, K**C<=1e18
        # 1 <= S <= K
        offset = 0
        for i in xrange(C):
            to_clean = []
            if K - i > 0:
                offset *= K
                offset += i
                for j in xrange(K-i):
                    to_clean.append(offset+j+1)
            else:
                offset *= K
                offset += K - 1
                to_clean.append(offset+1)
        if S < len(to_clean):
            print_output(OUTPUT % locals(), [IMP])
        else:
            print_output(OUTPUT % locals(), to_clean)

solve()

