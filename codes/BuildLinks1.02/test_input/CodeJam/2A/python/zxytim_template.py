#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $File: template.py
# $Date: Sat May 28 22:19:14 2016 +0800
# $Author: Xinyu Zhou <zxytim[at]gmail[dot]com>

import math
import numpy as np
import functools
import collections


@functools.lru_cache(maxsize=10000000)
def produce(winner, level):
    if level == 0:
        return winner
    else:
        oppo = dict(R='S', P='R', S='P')[winner]
        a = produce(winner, level - 1)
        b = produce(oppo, level - 1)
        if a < b:
            return a + b
        return b + a


def solve():
    N, R, P, S = map(int, input().split())
    ans = None
    for winner in ['R', 'P', 'S']:
        s = produce(winner, N)
        cnt = collections.Counter(list(s))
        if cnt['P'] == P and cnt['R'] == R and cnt['S'] == S:
            if ans is None or s < ans:
                ans = s
    if ans is None:
        print('IMPOSSIBLE')
    else:
        print(ans)

# print(solve())
nr_case = int(input().strip())

for case_id in range(1, nr_case + 1):
    print('Case #{}: '.format(case_id), end='')
    solve()


# vim: foldmethod=marker

