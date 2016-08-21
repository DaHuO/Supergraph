#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Google Code Jam: Round 1B 2016
#  Problem A. Getting the Digits
#
#  by xenosoz on May 1, 2016.
#

first = [
    ("G", "EIGHT", 8),
    ("U", "FOUR", 4),
    ("W", "TWO", 2),
    ("X", "SIX", 6),
    ("Z", "ZERO", 0),
]
second = [
    ("F", "FIVE", 5),
    ("H", "THREE", 3),
    ("O", "ONE", 1),
#    ("R", "THREE", 3),
    ("S", "SEVEN", 7),
#    ("T", "THREE", 3),
]
third = [    
    ("N", "NINE", 9),
]

def solve(S):
    from collections import Counter
    global first, second, third
    
    gene = Counter(S)
    solution = []
    for decoder in (first, second, third):
        for k, v, s in decoder:
            # We have #n values in our gene
            n = gene[k]
            if n > 0:
                n //= Counter(v)[k]
            solution.extend([s] * n)
            delta = Counter(v)
            for i in range(n):
                gene -= delta
    assert gene == Counter()

    return sorted(solution)

T = int(input())
for case in range(1, T+1):
    S = input()
    print(("Case #%d:" % case), ''.join(map(str, solve(S))))
