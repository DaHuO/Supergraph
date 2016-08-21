#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $File: a.py
# $Date: Sun May 01 00:22:39 2016 +0800
# $Author: Xinyu Zhou <zxytim[at]gmail[dot]com>

import math
import numpy as np
import collections
import functools


numstrs = [
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT",
    "NINE"]

charset = sorted(set(''.join(numstrs)))
charset_lut = {c: i for i, c in enumerate(charset)}
nr_chars = len(charset)

num_count = []
for s in numstrs:
    cnt = [0] * nr_chars
    for i in s:
        cnt[charset_lut[i]] += 1
    num_count.append(np.array(cnt))


class Found(Exception):
    pass


class Cache:
    def __init__(self):
        self.clear()

    def test(self, cnt):
        return tuple(cnt) in self._cache

    def put(self, cnt):
        self._cache.add(tuple(cnt))

    def clear(self):
        self._cache = set()

cache = Cache()


def can_sub(remain, conf):
    v = remain - conf
    if (v >= 0).all():
        return v, True
    return None, False

def is_empty(v):
    return v.sum() == 0

def do_solve(remain, i, cur_path):
    if cache.test(remain):
        return
    cache.put(remain)
    if is_empty(remain):
        raise Found()

#     print(cur_path)
#     print(remain)
#     print(num_count)

    for num, conf in zip(range(i, 10), num_count[i:]):
        subbed, rst = can_sub(remain, conf)
#         print(subbed, rst)
        if rst:
            cur_path.append(num)
            do_solve(subbed, i, cur_path)
            cur_path.pop()


def solve():
    s = input().strip()
    remain = [0] * nr_chars
    for i in s:
        remain[charset_lut[i]] += 1
    remain = np.array(remain)

    cache.clear()

    cur_path = []
    try:
        do_solve(remain, 0, cur_path)
    except Found as e:
        print(''.join(map(str, cur_path)))



# print(solve())
nr_case = int(input().strip())

for case_id in range(1, nr_case + 1):
    print('Case #{}: '.format(case_id), end='')
    solve()


# vim: foldmethod=marker

