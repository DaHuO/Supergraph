#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter

def RankAndFile():
    file = open("B-large.in")
    T = int(file.readline())

    out = open("B-large.out", "w")
    for t in range(T):
        N = int(file.readline())
        twoNone = 2 * N - 1
        soldiers = []
        cnt = set()
        for n in range(twoNone):
            lst = [int(x) for x in file.readline().split(' ')]
            for l in lst:
                soldiers.append(l)
                cnt.add(l)
        save = []
        soldiers.sort()
        # print Counter(soldiers).items()
        for (x, c) in Counter(soldiers).items():
            if c % 2 != 0:
                save.append(x)
        save.sort()
        f = "Case #{}: {}\n".format(t+1, ' '.join(str(s) for s in save))
        out.write(f)
        # print f,
    file.close()
    out.close()


if __name__ == '__main__':
    RankAndFile()
