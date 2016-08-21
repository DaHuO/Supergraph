#!/usr/bin/env python
#-*-coding: utf-8 -*-
import sys

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

nb = {0: "ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX",
      7 : "SEVEN", 8: "EIGHT", 9: "NINE"}
order = [0, 8, 6, 2, 3, 4, 1, 5, 7, 9]
letter = ['Z', 'G', 'X', 'W', 'H', 'R', 'O', 'F', 'S', 'N']

nb2 = dict()
for n in nb:
    nb2[n] = dict()
    for c in nb[n]:
        if c not in nb2[n]:
            nb2[n][c] = 0
        nb2[n][c] += 1

for t in xrange(1, T + 1):
    S = raw_input()
    res = list()
    multi = dict()
    for c in S:
        if c not in multi:
            multi[c] = 0
        multi[c] += 1
    for n, l in zip(order, letter):
        if l not in multi:
            continue
        b = True
        while multi[l] > 0 and b:
            b = True
            for c in nb2[n]:
                if c not in multi:
                    b = False
                    break
                if multi[c] < nb2[n][c]:
                    b = False
                    break
            if b:
                for c in nb2[n]:
                    multi[c] -= nb2[n][c]
                res.append(n)
    print "Case #%d: %s" % (t, ''.join(map(str,sorted(res))))
