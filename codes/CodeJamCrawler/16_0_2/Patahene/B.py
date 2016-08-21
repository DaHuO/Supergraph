#!/usr/bin/env python

import itertools
import os.path as path
from collections import namedtuple, Counter
import pprint
import numpy as np


def solve(n):
    pre = None
    norm = []
    for t in n:
        if t == pre:
            pass
        else:
            pre = t
            # print t
            norm.append(t)

    if len(norm) == 1 and norm[0] == '-':
        return 1

    c = 0
    b = '-'
    for t in norm[::-1]:
        if t == b:
            c += 1
            b = '+' if b == '-' else '-'

    return c

if __name__ == '__main__':
    ans = []
    with open('B-large.in') as f:
        T = int(f.readline())
        print T
        for i in xrange(T):
            n = f.readline().strip()
            ans.append(solve(n))


    with open('b_ans.txt', 'w') as f:
        for i, a in enumerate(ans, start=1):
            f.write('Case #%d: %s\n'%(i, a))

