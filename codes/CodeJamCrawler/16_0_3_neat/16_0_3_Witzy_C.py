# -*- coding: utf-8 -*-
"""
created by huash at 2016/4/9 09:43

"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections
import math

def str2number(digits, base):
    if not digits or base == 0:
        return 0

    result = 0
    m = 1
    for v in reversed(digits):
        result += m * int(v)
        m *= base

    return result

def divisor(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return i
    return -1


def isValid(digits):
    result = []
    for base in range(2, 11):
        d = divisor(str2number(digits, base))
        if d == -1:
            return []
        else:
            result.append(d)
    return result

def cal(digits, num):
    result = []
    while len(result) < num:
        ds = isValid(digits)
        if len(ds) > 0:
            result.append({digits: ds})
        digits = bin(str2number(digits, 2) + 2)[2:]
        #print(digits)
    return result

f = open("C-small-attempt0.in", "r")
output = open("C-small.out", "w")
T = f.readline()


i = 1
for line in f.readlines():
    N, J = map(int, line.split())
    digits = ['1']
    digits.extend(['0'] * (N-2))
    digits.append('1')
    result = cal(''.join(digits), J)

    output.write("Case #{}:\n".format(i))
    i += 1
    for p in result:
        for k,v in p.items():
            output.write("{} {}\n".format(k, " ".join(map(str, v))))

