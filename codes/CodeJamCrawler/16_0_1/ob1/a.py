#!/usr/bin/env python

import sys

def digits(n):
    return set(str(n))

def solve(n):
    d = set()
    for i in range(1, 10000):
        z = i*n
        d.update(digits(z))
        if len(d) == 10:
            return z
    return 'INSOMNIA'


if __name__=='__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    # print('Case #%d: %s' % (2, str(solve(int(lines[2])))))
    for i in range(1, n+1):
        print('Case #%d: %s' % (i, solve(int(lines[i]))))
