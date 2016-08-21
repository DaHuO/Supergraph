#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_digits(n):
    return [int(i) for i in str(n)]

def solve(n):
    # print("[debug] solving %s" % (n))
    if (n==0):
        return "INSOMNIA"

    seen = 0
    i = 1
    current = n
    while(seen != 0x3FF):
        current = n * i
        # print("[debug] current: %s" % (current))
        for d in get_digits(current):
            # print("[debug] digit: %s" % (d))
            seen = (1 << d) | seen

        # print("[debug] Seen: %s" % ("{0:b}".format(seen)))
        i = i + 1

    return current

if __name__ == "__main__":
    testcases = input()

    for i in xrange(1, testcases+1):
        n = int(raw_input())

        print("Case #%i: %s" % (i, solve(n)))