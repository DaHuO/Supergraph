#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(in_):
        n = int(in_)
        if n == 0:
                return 'INSOMNIA'
        digits = set()
        x = 1
        acc = 0
        while True:
                acc = n * x
                x += 1
                for i in str(acc):
                        digits.add(i)
                if len(digits) == 10:
                        return acc


if __name__ == "__main__":
        n = input()

        for c in xrange(1, n + 1):
                i = raw_input()
                print("Case #%i: %s" % (c, solve(i)))
