from __future__ import print_function

import sys

with open(sys.argv[1], 'r') as f:
    count = int(f.readline())
    cases = [c.strip() for c in f.readlines()]
    for i in range(count):
        res = 0
        case = (cases[i])[::-1]
        flip = False
        for p in case:
            if p == '-' and flip == False:
                flip = True
                res = res + 1
            if p == '+' and flip == True:
                flip = False
                res = res + 1
        print("Case #{}: {}".format(i+1, res))
