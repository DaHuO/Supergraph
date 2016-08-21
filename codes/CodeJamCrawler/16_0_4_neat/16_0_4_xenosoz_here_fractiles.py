#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Qualification Round 2016
# Problem D. Fractiles
#
# by xenosoz on Apr 10, 2016.
#

import math

def fractile_to_index(K, path):
    index = 0
    for p in path:
        index = index * K + max(0, p)
    return index + 1


def solve(K, C, S):
    groups = math.ceil(K/C)
    if groups > S:
        return "IMPOSSIBLE"

    elements = C * groups
    offset = K - elements
    indices = [fractile_to_index(K, range(C*g + offset, C*g + C + offset)) for g in range(groups)]
    
    return ' '.join(map(str, indices))


T = int(input())
for case_number in range(1, T+1):
    K, C, S = map(int, input().split())
    print("Case #%d:" % case_number, solve(K, C, S))
