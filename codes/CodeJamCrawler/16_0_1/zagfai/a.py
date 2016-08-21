#!/usr/bin/python
# -*- coding: utf-8 -*-
""" A
"""
__author__ = 'Zagfai'
__date__ = '2016-04'
__license__ = 'MIT'


def solve(num):
    if num == 0:
        return "INSOMNIA"
    multiple = 1
    sees = set()

    while len(sees)<10:
        sees |= set(list(str(multiple*num)))
        multiple += 1

    return num*(multiple-1)

n = int(raw_input())

for i in range(1, n+1):
    print "Case #%s: %s" % (i, solve(int(raw_input())))

