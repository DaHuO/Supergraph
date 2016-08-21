#!/usr/bin/env python

import os,sys


def solve(n):
    if n == 0:
        return "INSOMNIA"

    s = set(str(n))
    i = 1
    while len(s) < 10:
        i += 1
        s = s.union(set(str(i * n)))
    return i * n

lines = sys.stdin.readlines()
t = int(lines.pop(0))

for i in xrange(t):
    n = int(lines[i])
    #print (n)
    print("Case #" + str(i+1) + ": " + str(solve(n)))



