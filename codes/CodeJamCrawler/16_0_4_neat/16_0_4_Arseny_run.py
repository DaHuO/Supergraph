#!/usr/bin/env python

import sys


def solve(K, C, S):
    return " ".join(map(str, xrange(1, K + 1)))


if __name__ == '__main__':
    sys.stdin.readline()
    casenum = 0
    for line in sys.stdin:
        casenum+= 1
        K, C, S = map(int, line.split())
        answer = solve(K, C, S)
        print "Case #%s:" % casenum, answer