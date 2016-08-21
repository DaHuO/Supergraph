#! /usr/bin/env python
#-*- coding: utf-8 -*-
import sys,requests,json,os,traceback,datetime
reload(sys)
sys.setdefaultencoding('utf8')
from itertools import permutations

def spec_sort(a):
    l = len(a)
    if l == 1:
        return a

    mid = l / 2
    left = spec_sort(a[:mid])
    right = spec_sort(a[mid:])

    if left > right:
        return right + left
    else:
        return left + right

c = 'RPS'

T = int(raw_input())
for Case in range(1, T+1):
    inputs = map(int, raw_input().split(' '))
    n = inputs[0]
    rps = inputs[1:]

    # print permutations()

    best = None
    ans = []
    now = []
    for winner in range(3):
        ans = [winner]
        flag = True

        for i in xrange(n):
            now = []
            cnt = [0, 0, 0]
            for x in ans:
                y = (x+1)%3
                if c[x] < c[y]:
                    now.append(x)
                    now.append(y)
                else:
                    now.append(y)
                    now.append(x)
                cnt[x] += 1
                cnt[y] += 1
            for j, x in enumerate(cnt):
                if x > rps[j]:
                    # print 'BREAK', now
                    flag = False
            # print i, now
            ans = now

        if flag:
            ans = ''.join([ c[x] for x in ans ])

            # print 'found', ans
            # print 'sort', spec_sort(ans)

            ans = spec_sort(ans)
            if not best or ans < best:
                best = ans
    if best:
        print "Case #%d:" % Case, best
    else:
        print "Case #%d:" % Case, 'IMPOSSIBLE'
