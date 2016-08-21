#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    N, R, P, S = list(map(int, fin.readline().split()))

    r, p, s = R, P, S

    possible = True
    for i in range(N):
        a = (r + s - p) // 2
        b = (p + r - s) // 2
        c = (s + p - r) // 2
        if min(a, b, c) < 0:
            possible = False #'IMPOSSIBLE'
            break
        r = a
        p = b
        s = c
    if possible and r + p + s != 1:
        raise Exception("Something went wrong: %d %d %d" % (r, p, s))

    if not possible:
        print("Case #%d: %s" % (case, 'IMPOSSIBLE'))
    else:
        m = {'P': 'P', 'R': 'R', 'S': 'S'}
        for i in range(N):
            next = {}
            next['P'] = min(m['P'] + m['R'], m['R'] + m['P'])
            next['S'] = min(m['P'] + m['S'], m['S'] + m['P'])
            next['R'] = min(m['R'] + m['S'], m['S'] + m['R'])
            m = next
            debug(case, next)


        if r > 0:
            result = m['R']
        elif s > 0:
            result = m['S']
        elif p > 0:
            result = m['P']
        #result = (b * 'PR') + (c * 'PS') + (a * 'RS')
        print("Case #%d: %s" % (case, result))



