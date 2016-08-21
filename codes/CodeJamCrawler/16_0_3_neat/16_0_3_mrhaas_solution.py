#!/usr/bin/env python

import sys
import math

def getDivisor(n):
    for i in xrange(2, int(math.sqrt(n+1)) + 1):
        if n % i == 0:
            return i

def solve(n, j):
    frm = int("1%s1" % ("0" * (n-2), ), 2)
    to = int("1%s1" % ("1" * (n-2), ), 2)

    sols = {}

    for x in xrange(frm, to + 1, 2):
        if len(sols) == j:
            break

        b = bin(x)[2:]
        divisors = ()
        for base in xrange(2, 11):
            divisors += (getDivisor(int(b, base)),)
        if all(divisors):
            sols[b] = divisors
    return "\n".join("%s %s" % (b, " ".join([str(l) for l in divisors])) for b, divisors in sols.iteritems())

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for i in xrange(n):
        N, J = [int(c) for c in sys.stdin.readline().split(" ")]
        print "Case #%d:\n%s" % (i+1, solve(N, J))
