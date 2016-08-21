# -*- coding: utf-8 -*-
from itertools import groupby

__author__ = 'kaalroca'


def pancakes(pan):
    list_unique = [x[0] for x in list(groupby(pan))]

    if '-' not in list_unique:
        return 0
    elif list_unique[-1] == '+':
        return len(list_unique[:-1])
    else:
        return len(list_unique)

t = int(raw_input())
for i in range(1, t + 1):
    pan = raw_input()
    print "Case #{}: {}".format(i, pancakes(pan))

