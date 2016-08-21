#!/usr/bin/env python

import sys

def solve(n):
    if n == 0:
        return "INSOMNIA"

    found = {}
    i = 0

    while len(found.items()) < 10:
        x = str(n * (i + 1))
        for c in x:
            found[c] = True
        i += 1

    return i * n

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for i in xrange(n):
        N = int(sys.stdin.readline())
        print "Case #%d: %s" % (i + 1, solve(N))
