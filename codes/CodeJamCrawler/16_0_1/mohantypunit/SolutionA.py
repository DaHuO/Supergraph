#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def solve(N):
    """

    :param N:
    :return:
    """
    setofnums = set()
    newN = int(N)
    i = 1
    while len(setofnums) < 10:
        for x in str(newN):
            setofnums.add(x)
        if len(setofnums) == 10:
            return newN
        elif newN == 0:
            return "INSOMNIA"
        elif newN >= sys.maxint/100:
            return "INSOMNIA"
        i += 1
        newN = i * int(N)
if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))

