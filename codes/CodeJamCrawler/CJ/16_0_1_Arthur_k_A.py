#!/usr/local/bin/python3
import numpy as np
c = int(input())

ns = np.array([int(input()) for case in range(c)])


def solve(v):
    if v == 0:
        return "INSOMNIA"

    check = set(range(10))
    ov, v = v, 0

    while len(check) > 0:
        v += ov
        cc = set([int(i) for i in str(v)])
        check -= cc

    return v

vfunc = np.vectorize(solve)

for case, item in enumerate(vfunc(ns)):
    print ('Case #{}: {}'.format(case + 1, item))
