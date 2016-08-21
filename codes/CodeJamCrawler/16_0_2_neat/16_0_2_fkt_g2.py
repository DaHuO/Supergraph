#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(s):
    s = list(s)
    n = 0
    while True:
        last_sad = ''.join(s).rfind('-')
        if last_sad < 0:
            return n
        n += 1
        for i in xrange(last_sad + 1):
            if s[i] == '+':
                s[i] = '-'
            else:
                s[i] = '+'

if __name__ == "__main__":
        n = input()

        for c in xrange(1, n + 1):
                i = raw_input()
                print("Case #%i: %s" % (c, solve(i)))
