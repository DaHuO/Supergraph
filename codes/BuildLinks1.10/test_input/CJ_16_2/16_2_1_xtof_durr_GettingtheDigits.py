#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# google code jam - c.durr - 2016
# GettingtheDigits
# https://code.google.com/codejam/contest/11254486/dashboard
# solve a linear equation system

from sys import stdin
from collections import Counter
from string import ascii_uppercase
from tryalgo.gauss_jordan import gauss_jordan  # tryalgo is available at pypi


def readint(): return int(stdin.readline())
def readints(): return list(map(int, stdin.readline().split()))
def readstr(): return stdin.readline().strip()


def countletters(s):
    c = Counter()
    for x in s:
        c[x] += 1
    return c


word = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def solve(s):
    scount = countletters(s)
    A = []
    b = []
    # generate length constraint
    row = [0] * 10
    for d in range(10):
        row[d] = len(word[d])
    A.append(row)
    b.append(len(s))
    # generate letter constraint
    wordcount = [countletters(w) for w in word]
    for x in ascii_uppercase:
        row = [0] * 10
        for d in range(10):
            row[d] = wordcount[d][x]
        A.append(row)
        b.append(scount[x])
    sol = [0] * 10
    gauss_jordan(A, sol, b)
    res = ""
    for d in range(10):
        res += str(d) * int(sol[d] + 0.5)
    return res


for test in range(readint()):
    print('Case #%d: %s' % (test + 1, solve(readstr())))
