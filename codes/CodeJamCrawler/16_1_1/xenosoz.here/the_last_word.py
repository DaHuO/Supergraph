#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Round 1A 2016
# Problem A. The Last Word
#
# by xenosoz on Apr 16, 2016.
#

def solve(S):
    word = ""
    for s in S:
        left = s + word
        right = word + s
        word = max(left, right)
    return word

T = int(input())

for case_id in range(1, T+1):
    S = input()
    print("Case #%d:" % case_id, solve(S))
