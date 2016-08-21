#!/usr/bin/python

T = int(raw_input())

CASE = 1

while T > 0:
    T -= 1

    N = int(raw_input())
    digits = set()
    ret = 0

    if N > 0:
        L = 1
        while len(digits) < 10:
            Q = N * L
            for ch in str(Q):
                digits.add(ch)
            L += 1
        ret = Q

    if ret == 0:
        ret = 'INSOMNIA'

    print 'Case #%d:' % CASE, ret
    CASE += 1
