#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def flip_symbol(c):
    return '+' if c == '-' else '-'


def solve(S):
    toflip = '-'
    toskip = '+'
    N = 0
    for c in reversed(S):
        if c == toskip:
            continue
        if c == toflip:
            N += 1
            toflip = flip_symbol(toflip)
            toskip = c
    return N


T = int(ifs.readline())
for t in range(1, T + 1):
    S = ifs.readline().strip()
    a = solve(S)
    ofs.write('Case #%s: %d\n' % (t, a))
