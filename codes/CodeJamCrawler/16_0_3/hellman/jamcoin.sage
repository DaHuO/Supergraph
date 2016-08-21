#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sage.all import *

import sys, math, random, operator
from itertools import product, permutations, combinations
from collections import deque, defaultdict, Counter

raw_input = lambda: sys.stdin.readline().rstrip()
pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
epr = lambda *args: sys.stderr.write(" ".join(str(x) for x in args) + "\n")
die = lambda *args: pr(*args) ^ exit(0)

read_str = raw_input
read_strs = lambda: raw_input().split()
read_int = lambda: int(raw_input())
read_ints = lambda: map(int, raw_input().split())
read_float = lambda: float(raw_input())
read_floats = lambda: map(float, raw_input().split())

"---------------------------------------------------------------"

def calc_divs(x):
    divs = []
    for b in range(2, 11):
        val = int(x, b)
        for p, e in factor(val):
            if p != val:
                divs.append(p)
                break
        else:
            return []
    return divs

seen = set()

def solve(N, J):
    while J:
        x = random.getrandbits(N - 2)
        x = "1" + bin(x)[2:].rjust(N - 2, "0") + "1"
        if x in seen:
            continue
        seen.add(x)
        divs = calc_divs(x)
        if len(divs) == 9:
            epr(x, [int(x, b) for b in range(2, 11)], divs)
            for b, d in zip(range(2, 11), divs):
                assert int(x, b) % d == 0
                assert int(x, b) != d
            # quit()
            yield x, divs
            J -= 1

t = read_int()
for t in xrange(t):
    N, J = read_ints()
    print "Case #%d:" % (t + 1)
    for c, ds in solve(N, J):
        pr(c, *ds)
