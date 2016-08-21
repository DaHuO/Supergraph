#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def digits_seq(n, base=10):
    if n < 0:
        n = -n
    while True:
        n, m = divmod(n, base)
        yield m
        if n == 0:
            break


INSOMNIA = 'INSOMNIA'
max_iterations = 100

def solve(N):
    if N == 0:
        return INSOMNIA
    D = set(digits_seq(N))
    k = 1
    s = N
    while len(D) < 10:
        s += N
        D.update(set(digits_seq(s)))
        k += 1
        if k >= max_iterations:
            return INSOMNIA
    return s


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


T = int(ifs.readline())
for t in range(1, T + 1):
    N = int(ifs.readline())
    a = solve(N)
    ofs.write('Case #%s: %s\n' % (t, str(a)))
