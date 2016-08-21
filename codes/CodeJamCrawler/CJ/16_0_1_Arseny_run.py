#!/usr/bin/env python

import sys


def digits(k):
    result = set()
    while (k > 0):
        result.add(k % 10)
        k = k / 10
    return result


def solve(x):
    seen = set()
    for i in xrange(1, 100):
        seen.update(digits(i * x))
        if len(seen) == 10:
            return i * x
    return None


if __name__ == '__main__':
    sys.stdin.readline()
    casenum = 0
    for line in sys.stdin:
        casenum+= 1
        N = int(line)
        answer = solve(N)
        print "Case #%s:" % casenum, ('INSOMNIA' if (answer is None) else answer)
