#!/usr/bin/env python

def divisor(i, maxv):
    d = 2
    while d*d <= i and d < maxv:
        if i % d == 0:
            return d
        d += 1
    return None

def check(i):
    res = []
    for s in range(2,11):
        d = divisor(int(i, s), 100)
        if d is None:
            return None
        res.append(d)
    return res

def solve(N, J):
    j = 0
    n = 2**(N-1)+1
    while j < J:
        b = "{0:b}".format(n)
        ds = check(b)
        if ds is not None:
            print b, ' '.join(str(d) for d in ds)
            j += 1
        n = n + 2

print 'Case #1:'
solve(32, 500)
