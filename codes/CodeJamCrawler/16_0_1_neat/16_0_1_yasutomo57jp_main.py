#!/usr/bin/env python

from __future__ import print_function
import sys

T = int(sys.stdin.readline().strip())


def check(N):
    i = 1
    c = set([])
    a = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if N == 0:
        return "INSOMNIA"
    while True:
        num = N * i
        t = str(num)
        for r in t:
            c.add(r)
        if len(c.symmetric_difference(a)) == 0:
            return num
        i += 1


case = 1
while True:
    s = sys.stdin.readline().strip()
    if s == "":
        break
    N = int(s)

    result = check(N)

    print("Case #%d: %s" % (case, result))

    case += 1
