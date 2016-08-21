#!/usr/bin/env python2

import math
import itertools

def inbase(n, base):
    tot = 0
    for i in xrange(len(n)):
        if n[len(n)-i-1] == '1':
            tot += base**i
    return tot

def divisor(n):
    if n == 1 or n == 2:
        return None

    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return i
    return None

def solve(N, J):
    for k in itertools.product('01', repeat=N-2):
        c = ('1',) + k + ('1',)
        jamcoin = True
        divisors = ""
        for base in xrange(2, 10+1):
            c_b = inbase(c, base)
            d = divisor(c_b)
            if not d:
                jamcoin = False
                break
            divisors += " %s" % d
        if jamcoin:
            print '%s%s' % (''.join(c), divisors)
            J -= 1
        if not J:
            break

T = int(raw_input())
for i in xrange(1, T+1):
    N, J = [int(x) for x in raw_input().split()]
    print "Case #%s:" % i
    solve(N, J)
