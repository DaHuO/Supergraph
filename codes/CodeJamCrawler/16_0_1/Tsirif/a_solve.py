#!/usr/bin/env python
# encoding: utf-8

"""
Submission for problem A: Counting Sheep
of Google CodeJam 2016

Author: Tsirigotis Christos <tsirif@gmail.com>
Date: April 09, 2016
"""


OUTPUT = "Case #%(nc)s: %(L)s"
find_digits = lambda x: set(map(int, list(str(x))))
ALL_DIGITS = find_digits(1234567890)

def solve():
    T = int(raw_input()) # 1 <= T <= 100
    for nc in xrange(1, T+1):
        N = int(raw_input()) # 0 <= N <= 200 <= 1e6
        if N == 0:
            L = "INSOMNIA"
            print(OUTPUT % locals())
        else:
            i = 0
            digits_seen = set([])
            while digits_seen != ALL_DIGITS:
                i += 1
                L = i * N
                digits_seen |= find_digits(L)
            print(OUTPUT % locals())

solve()

