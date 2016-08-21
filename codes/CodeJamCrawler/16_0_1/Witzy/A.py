# -*- coding: utf-8 -*-
"""
created by huash at 2016/4/9 08:32

"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections



def getDigits(num):
    result = set()
    while num > 0:
        result.add(num % 10)
        num /= 10
    return result

def lastNumber(num):
    baseDigits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    visitedNums = set()
    v = num
    while v not in visitedNums:
        baseDigits = baseDigits - getDigits(v)
        if len(baseDigits) == 0:
            return v
        visitedNums.add(v)
        v += num

    return "INSOMNIA"

f = open("A-large.in", "r")
output = open("A-large.out", "w")
T = f.readline()

i = 1
for num in f.readlines():
    output.write("Case #{}: {}\n".format(i, lastNumber(int(num))))
    i += 1



