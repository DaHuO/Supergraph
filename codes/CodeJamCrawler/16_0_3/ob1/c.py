#!/usr/bin/env python

import sys
from math import sqrt

def find_divisor(n):
    for i in range(2, 1000):
        if n%i == 0:
            return i
    return None

def check_coin(c):
    proof = []
    for i in range(2, 11):
        d = find_divisor(int(c, i))
        if d:
            proof.append(d)
        else:
            return None
    return proof
            

def solve(n, j):
    print('Case #1:')
    k = 0
    for i in range(1 << (n-2)):
        c = 1<<(n-1) | i<<1 | 1
        cs = '{0:b}'.format(c)
        proof = check_coin(cs)
        if proof:
            print(cs, ' '.join([str(p) for p in proof]))
            k += 1
            if k >= j:
                return


if __name__=='__main__':
    solve(32, 500)
