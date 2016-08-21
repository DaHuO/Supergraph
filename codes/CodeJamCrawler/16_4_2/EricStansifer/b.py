# Python 3.5.1

from common import *
import numpy as np

def comp(ps):
    x = np.array([1])
    for p in ps:
        x = (np.array(list(x) + [0]) * (1 - p)) + (np.array([0] + list(x)) * p)
    return float(x[len(ps) // 2])

def main(casenum):
    n, k = readints()
    ps = readfloats()
    ps.sort()

    best = 0
    for a in range(k + 1):
        q = comp(ps[:a] + ps[n-(k-a):])
        if q > best:
            best = q
    writecase(casenum, best)

run(main)
