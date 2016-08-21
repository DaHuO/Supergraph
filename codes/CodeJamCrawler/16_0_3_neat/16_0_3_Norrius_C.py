#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import sys

n = 16
j = 500

a = 0b10000000000000000000000000000001

def primecheck(a):
    for i in range(2, 300):
        if (a % i) == 0:
            return i
    return None

c = 0

print("Case #1:")

while c != j:
    div = []
    for b in range(2, 11):
        d = primecheck(int(format(a, 'b'), b))
        if d:
            div.append(d)
        else:
            break
    else:
        print(format(a, 'b'), ' '.join(map(str, div)))
        sys.stdout.flush()
        c += 1
    a += 2