#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    N, *data = f.read().splitlines()
    for i in range(len(data)):
        S = data[i]
        res = ''
        for c in S:
            if res == '':
                res = c[:]
            else:
                a = res+c
                b = c+res
                res = max(a,b)
        print("Case #{}: {}".format(i+1, res))