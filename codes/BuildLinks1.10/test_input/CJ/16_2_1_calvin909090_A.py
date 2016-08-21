#!/usr/bin/env python3
import numpy as np
from collections import Counter
mapping = {'E': 2,
           'F': 7,
           'G': 3,
           'H': 4,
           'I': 12,
           'N': 5,
           'O': 13,
           'R': 11,
           'S': 8,
           'T': 10,
           'U': 6,
           'V': 0,
           'W': 1,
           'X': 9,
           'Z': 14}

nums = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
d = np.zeros((10, len(mapping)))
for i, num in enumerate(nums):
    for k, v in Counter(num).items():
        d[i, mapping[k]] = v

d = d.T

def solve(s):
    c = Counter(s)
    a = np.zeros(len(mapping))
    for k, v in c.items():
        a[mapping[k]] = v

    r = np.linalg.lstsq(d, a)
    if r[1] > 1:
        raise
    res = np.rint(r[0])
    s = []
    for i, j in enumerate(res):
        s.append(str(i)*j)
    return ''.join(s)

T = int(input())
for i in range(T):
    print("Case #%d:" % (i+1), solve(input()))
