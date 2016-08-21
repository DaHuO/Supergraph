#!/usr/local/bin/python3
import numpy as np
from collections import Counter
c = int(input())


def convert(s, n):
    s = str(s)
    return "0" * (n - len(s)) + s


def possible(cc, target):
    cc = convert(cc, len(target))

    for i in range(len(cc)):
        if target[i] != "?" and cc[i] != target[i]:
            return False

    return True


def solve():
    s1, s2 = input().strip().split()

    n = len(s1)
    g = [(i, j, abs(i - j)) for i in range(10**n) for j in range(10**n)]
    g.sort(key=lambda x: x[2])

    result = None
    for elem in g:
        if (not result is None) and (elem[2] > result[2]):
            break
        if possible(elem[0], s1) and possible(elem[1], s2):
            if result is None:
                result = elem
            elif elem[2] < result[2]:
                result = elem
            elif elem[2] == result[2] and elem[1] + elem[0] < result[1] + result[0]:
                result = elem

    return convert(result[0], n) + " " + convert(result[1], n)

for case in range(c):
    print ('Case #{}: {}'.format(case + 1, solve()))
