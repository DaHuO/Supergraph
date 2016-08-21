#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def solver(n):
    check = np.zeros(10, np.bool)

    if n == 0:
        return -1
    iter = 0
    while sum(check)<10:
        str_n = str((iter+1)*n)
        for k in xrange(len(str_n)):
            digit = int(str_n[k])
            check[digit] = True
        iter += 1

    return (iter)*n

if __name__ == "__main__":

    testcases = input()

    for caseNr in xrange(1, testcases+1):
        n = input()
        o = solver(n)
        if o>0:
            print("Case #%i: %s" % (caseNr, o))
        else:
            print "Case #%i: INSOMNIA" % caseNr