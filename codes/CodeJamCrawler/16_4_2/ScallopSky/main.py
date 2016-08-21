#! /usr/bin/env python
#-*- coding: utf-8 -*-
import sys,requests,json,os,traceback,datetime
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')

def calc(p, k):
    f = np.zeros((k + 1, k + 1))
    f[0][0] = 1.0
    for i in xrange(1, k+1):
        for j in xrange(0, k+1):
            # print i, j
            if j == 0:
                f[i][j] = f[i-1][j] * (1 - p[i-1])
            else:
                f[i][j] = f[i-1][j-1] * p[i-1] + f[i-1][j] * (1 - p[i-1])
    return f[k][k/2]

T = int(raw_input())
for Case in range(1, T+1):
    inputs = map(int, raw_input().split(' '))
    n = inputs[0]
    k = inputs[1]
    p = map(float, raw_input().split(' '))

    p.sort()
    ans = calc(p[:k/2] + p[len(p) - k/2:], k)

    pp = p + p
    for start in range(n):
        p = pp[start:start+k]
        now = calc(p, k)

        if now > ans:
            # print p, now
            ans = now

    # print f

    print "Case #%d:" % Case, "%.8f" % ans
