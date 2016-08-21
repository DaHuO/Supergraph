#!/usr/bin/env python

import itertools
import os.path as path
from collections import namedtuple, Counter
import pprint
import numpy as np

def solve(n):
    # print '---------------', n
    digit = map(str, range(10))
    y = n
    for i in xrange(100):
        dl = []
        stry = str(y)
        for d in digit:
            if d in stry:
                dl.append(d)
        for d in dl:
            digit.remove(d)
        # print digit
        if not digit:
            print y, y/n
            return y

        y += n

    return 'INSOMNIA'



if __name__ == '__main__':
    ans = []
    with open('A-large.in') as f:
        T = int(f.readline())
        print T
        for i in xrange(T):
            ans.append(solve(int(f.readline())))

    with open('ans.txt', 'w') as f:
        for i, a in enumerate(ans, start=1):
            f.write('Case #%d: %s\n'%(i, a))

    # for i in xrange(1, 1000000):
    #     solve(i)
