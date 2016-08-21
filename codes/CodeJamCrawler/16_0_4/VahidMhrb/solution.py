#!/usr/bin/env python

import sys

def solve(k, c, s):
    return " ".join(str(1 + x * k**(c-1)) for x in xrange(k))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in xrange(n):
        K, C, S = (int(c) for c in sys.stdin.readline().split(" "))

        print "Case #%d: %s" % (i + 1, solve(K, C, S))
