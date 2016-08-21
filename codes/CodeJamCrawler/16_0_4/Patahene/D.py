#!/usr/bin/env python

import itertools
import os.path as path
from collections import namedtuple, Counter
import pprint


def solve(k, c, s):
    return ' '.join([str(i+1) for i in xrange(k)])

if __name__ == '__main__':
    ans = []
    with open('D-small-attempt1.in') as f:
        T = int(f.readline())
        print T
        for i in xrange(T):
            k, c, s = map(int, f.readline().strip().split())
            ans.append(solve(k, c, s))


    with open('d_ans.txt', 'w') as f:
        for i, a in enumerate(ans, start=1):
            f.write('Case #%d: %s\n'%(i, a))

