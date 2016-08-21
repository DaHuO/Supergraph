# -*- coding: utf-8 -*-
"""
created by huash at 2016/4/9 09:10

"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections


def reverse(cake):
    if not cake:
        return []

    result = []
    for c in reversed(cake):
        if c == '+':
            result.append('-')
        else:
            result.append('+')

    return result

def cal(cake):
    if not cake:
        return 0

    l = 0
    r = len(cake) - 1

    while r > l and cake[r] == '+':
        r -= 1
    r += 1

    result = 0

    while l < r:
        while l < r and cake[l] == '+':
            l += 1
        if l < r:
            if l > 0:
                result += 1
            while l < r and cake[l] == '-':
                l += 1
            if l < r:
                result += 1 + cal(reverse(cake[l:r]))
            else:
                result += 1
            break
        else:
            break
    return result


f = open("B-large.in", "r")
output = open("B-large.out", "w")
T = f.readline()


i = 1
for cake in f.readlines():
    output.write("Case #{}: {}\n".format(i, cal(cake.strip())))
    i += 1
