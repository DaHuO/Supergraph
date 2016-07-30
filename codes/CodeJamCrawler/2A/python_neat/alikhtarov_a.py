#!/usr/bin/env python

import sys
ls = sys.stdin.readlines()[1:]

name = ['R', 'P', 'S']

def f(left, i, r):
    opp = (i - 1 + 3) % 3
    if left[i] == 0 or left[opp] == 0:
        return None
    if r == 0:
        left[i] -= 1
        left[opp] -= 1
        return name[i] + name[opp]

    out = f(left, i, r - 1)
    if out is None:
        return None
    out2 = f(left, opp, r - 1)
    if out2 is None:
        return None
    return out + out2

def ss(s):
    if len(s) == 1:
        return s
    left = ss(s[:len(s)/2])
    right = ss(s[len(s)/2:])
    if left < right:
        return left+right
    else:
        return right + left

C = 1
for line in ls:
    n, nr, np, ns = [int(x) for x in line.split()]

    out = None

    for i in range(3):
        s = f([nr, np, ns], i, n-1)
        if s is not None:
            s = ss(s)
            if out is None or s < out:
                out = s

    if out is None:
        out = "IMPOSSIBLE"

    print "Case #%d: %s" % (C, out)
    C += 1
