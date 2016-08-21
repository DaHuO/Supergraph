#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter

T = int(raw_input())

for case in range(1, T + 1):
    N = int(raw_input())
    twoNone = 2 * N - 1
    soldiers = []
    cnt = set()
    for n in range(twoNone):
        mylist = map(int, raw_input().strip().split())
        for l in mylist:
            soldiers.append(l)
            cnt.add(l)

    save = []
    soldiers.sort()
    for (x, c) in Counter(soldiers).items():
        if c % 2 != 0:
            save.append(x)
    save.sort()

    print "Case #{}: {}".format(case, ' '.join(str(s) for s in save))
