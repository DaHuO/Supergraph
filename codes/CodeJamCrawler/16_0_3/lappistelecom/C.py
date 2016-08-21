#!/usr/bin/env python
#-*-coding: utf-8 -*-
import math
import sys
from random import randint

def get_divisor(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, min(int(math.sqrt(n)), 100000), 2):
        if n % i == 0:
            return i
    return -1

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

def create_number(N):
    res = '1'
    for i in range(N - 2):
        res += str(randint(0,1))
    if N >= 2:
        res += '1'
    return res

def base(n, b):
    bmax = len(n)
    res = 0
    for c in n:
        bmax -= 1
        res += int(c) * (b**bmax)
    return res

for t in range(T):
    N, J = readarray(int)
    print "Case #%d:" % (t+1)
    res = set()
    for j in range(J):
        found = False
        while not found:
            n = create_number(N)
            sol = list()
            if n in res:
                continue
            for b in range(2, 11):
                nb = base(n, b)
                divisor = get_divisor(nb)
                if divisor > 0:
                    sol.append(divisor)
                else:
                    break
            if len(sol) == 9:
                found = True
        mystr = n
        for d in sol:
            mystr += " " + str(d)
        print mystr
