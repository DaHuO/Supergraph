#!/usr/bin/env python
import sys


def print_ans(i, a):
    print("Case #{0}: {1}".format(i, a))

lines = sys.stdin.readlines()

for i, l in enumerate(lines[1:], start=1):
    cakes = l.strip()

    n = 0
    prev = None
    for c in cakes:
        if c == '-':
            if prev is None:
                n += 1
            elif c != prev:
                n += 2
        prev = c
    print_ans(i, n)
