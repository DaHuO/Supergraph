#!/usr/bin/env python

import sys

def solve(s):
    curr = '+'
    n = 0
    for i in reversed(s):
        if i in ['-', '+']:
            if i != curr:
                curr = i
                n += 1
    return n


if __name__=='__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    for i in range(1, n+1):
        print('Case #%d: %d' % (i, solve(lines[i])))
