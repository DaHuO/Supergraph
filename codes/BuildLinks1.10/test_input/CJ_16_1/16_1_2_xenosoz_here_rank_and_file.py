#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Round 1A 2016
# Problem B. Rank and File
#
# by xenosoz on Apr 16, 2016.
#

from collections import Counter

def solve():
    N = int(input())
    counter = Counter()
    for n in range(N*2-1):
        counter.update(input().split())
        
    f = lambda x: x[1] % 2==1
    m = lambda x: int(x[0])
    return ' '.join(map(str, sorted(map(m, filter(f, counter.items())))))

T = int(input())

for case_id in range(1, T+1):
    print("Case #%d:" % case_id, solve())
