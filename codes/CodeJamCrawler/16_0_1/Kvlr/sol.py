#-*- coding: utf-8 -*-

T = int(raw_input())

def digits(n):
    return set([int(d) for d in str(n)])

def solve():
    n = int(raw_input())
    if n == 0:
        return "INSOMNIA"

    k = n
    seen_digits = digits(n)
    while len(seen_digits) < 10:
        k = k + n
        seen_digits = seen_digits.union(digits(k))

    return str(k)

for tn in xrange(1,T+1):
    print "Case #%d: %s" % (tn, solve())
