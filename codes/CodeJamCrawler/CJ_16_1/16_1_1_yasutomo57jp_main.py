#!/usr/bin/env python

from __future__ import print_function
import sys

T = int(sys.stdin.readline().strip())


def check(S):
    slist = list(S)

    result = []
    for c in slist:
        if len(result) == 0:
            result.append(c)
        elif result[0] <= c:
            result.insert(0, c)
        else:
            result.append(c)

    return "".join(result)

case = 1
while True:
    s = sys.stdin.readline().strip()
    if s == "":
        break
    result = check(s)

    print("Case #%d: %s" % (case, result))

    case += 1
