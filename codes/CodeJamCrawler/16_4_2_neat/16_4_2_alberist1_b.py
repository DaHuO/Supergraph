#!/usr/bin/python3
# -*- coding: utf-8 -*-
import itertools


def solve():
    n, k = map(int, input().split())
    p = map(float, input().split())
    mx = 0
    for v in itertools.combinations(p, k):
        vs = [0 for _ in range(k+1)]
        vs[0] = 1
        for j, x in enumerate(v):
            for i in range(k, 0, -1):
                vs[i] = vs[i] * (1 - x) + vs[i-1] * x
            vs[0] *= 1 - x
        mx = max(mx, vs[k//2])
    return "%.10f" % mx


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print('Case #%d:' % (i+1), solve())
