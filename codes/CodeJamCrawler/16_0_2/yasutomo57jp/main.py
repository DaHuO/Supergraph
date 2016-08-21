#!/usr/bin/env python

from __future__ import print_function
import sys

T = int(sys.stdin.readline().strip())


def check_diff(s, k):
    l = len(s)
    for i in range(l, 0, -1):
        if s[i-1] != k:
            return i


def check_minus(s):
    k = s[-1]
    d = check_diff(s, k)
    if d is None:
        if k == "-":
            return 0
        else:
            return 1
    if k == "-":
        return check_minus(s[:d])
    else:
        return check(s[:d])+1


def check(s):
    k = s[-1]
    d = check_diff(s, k)
    if d is None:
        if k == "-":
            return 1
        else:
            return 0
    if k == "-":
        return check_minus(s[:d]) + 1
    else:
        return check(s[:d])


for case in range(T):
    s = sys.stdin.readline().strip()
    if s == "":
        break

    result = check(list(s))

    print("Case #%d: %s" % (case+1, result))
