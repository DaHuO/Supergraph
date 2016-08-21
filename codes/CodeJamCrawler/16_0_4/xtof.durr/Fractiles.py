#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# google code jam - c.durr - 2016
# Fractiles

"""Say G=0, L=1
  say original sequence is a bit sequence X_0, x_1, .., X_{K-1}, then
  in the final sequence every bit corresponds to a monomial of
             (X_0 + ... + X_{K-1})^C.
  The i-th bit in the final sequence (i starts at 0) is
  X_{a_{c-1}} * ... * X_{a_0} where i = a_{c-1}...a_{0} in base K.
  Hence ceil(K/C) queries are necessary and sufficient to select
  monomials that contain all K bits.

  Example C=2, K=5, we will select monomials
  X0X1 at index 01 in base 5 = 1 (need to add 1 for output)
  X2X3 at index 23 in base 5 = 2*5+3 = 13
  X4X4 at index 44 in base 5 = 4*5+4 = 24
"""

from sys import stdin


def readint(): return int(stdin.readline())
def readints(): return list(map(int, stdin.readline().split()))
def readstr(): return stdin.readline().strip()


def solve(K, C):
    sol = []
    i = -1
    while True:
        pos = 0
        KpowJ = 1
        for j in range(C):
            i = min(i + 1, K - 1)
            pos += i * KpowJ
            KpowJ *= K
        sol.append(pos + 1)
        if i == K - 1:
            break
    return sol

for test in range(readint()):
    K, C, S = readints()
    sol = solve(K, C)
    print('Case #%d: ' % (test+1), end="")
    if len(sol) <= S:
        print(" ".join(map(str, sol)))
    else:
        print("IMPOSSIBLE")
