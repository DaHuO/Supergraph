#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import sys

T = int(sys.stdin.readline().strip())

A = [chr(i) for i in range(65,65+26)]


def remove2(p, idx, mjn2):
    pp = p.copy()
    pp[idx[0][0]] -= 2

    if np.any(pp > mjn2):
        return False, []
    else:
        return True, pp

def remove11(p, idx, mjn2):
    pp = p.copy()
    pp[idx[0][0]] -= 1
    pp[idx[1][0]] -= 1

    if np.any(pp > mjn2):
        return False, []
    else:
        return True, pp


def check(N, s):
    result = ""
    p = np.array(map(int, s.split(" ")))

    while True:
        #print(p)
        sp = sum(p)
        if sp == 0:
            break

        mjn1 = (sp-1) / 2
        mjn2 = (sp-2) / 2

        idx = sorted(enumerate(p), key=lambda x: x[1], reverse=True)
        #print(idx)

        if idx[0][1] >= 2:
            st, pp = remove2(p, idx, mjn2)
            if st:
                p = pp
                result += " " + A[idx[0][0]] + A[idx[0][0]]
                continue
        if idx[0][1] >= 1 and idx[1][1] >= 1:
            st, pp = remove11(p, idx, mjn2)
            if st:
                p = pp
                result += " " + A[idx[0][0]] + A[idx[1][0]]
                continue
        p[idx[0][0]] -= 1
        result += " " + A[idx[0][0]]

    return result


case = 1
while True:
    N = sys.stdin.readline().strip()
    s = sys.stdin.readline().strip()
    if s == "":
        break
    result = check(N, s)

    print("Case #%d:%s" % (case, result))

    case += 1
