#!/usr/bin/python3

import sys
import numpy as np
from collections import Counter

DEBUG = True
def debug(*s):
    if DEBUG:
        print(*s, file=sys.stderr)

if __name__ == '__main__':
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    col = ['ZERO', 'ONE', 'TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
    m = []
    for _ in range(26):
        m.append([0] * 10)
    for w in col:
        for c in w:
            m[alpha.index(c)][col.index(w)] += 1

    T = int(input())
    for case in range(1, T+1):
        s = input()
        b = [0] * 26
        for c in s:
            b[alpha.index(c)] += 1
        x = np.round(np.linalg.lstsq(m, b)[0])
        result = ""
        for i in range(10):
            result += str(i) * x[i]


        print("Case #{}: {}".format(case, result))
        print("Case #{}: {}".format(case, result), file=sys.stderr)
