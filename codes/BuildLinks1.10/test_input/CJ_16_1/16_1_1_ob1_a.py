#!/usr/bin/env python

import sys

def solve(s):
    m = s[0]
    res = ""
    res += m
    for c in s[1:]:
        if c >= m:
            m = c
            res = c + res
        else:
            res = res + c
    return res


if __name__=='__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    # print('Case #%d: %s' % (2, str(solve(int(lines[2])))))
    for i in range(1, n+1):
        print('Case #%d: %s' % (i, solve(lines[i][:-1])))
