#!/usr/bin/env python3
import numpy as np

def div(n):
    for div in range(2, int(n**0.5) + 1):
        if not n % div:
            return div
    return 0

def jams(s):
    for jam in range(2**(s-1) + 1, 2**s):
        if jam & 1:
            yield bin(jam).lstrip('0b')

T = int(input())
for i in range(1, T+1):
    N, J = map(int, input().strip().split())

    print("Case #%d:" % i)
    printed = 0
    for jam in jams(N):
        dividers = np.array([div(int(jam, base)) for base in range(2, 11)])
        if np.all(dividers):
            print("{} {}".format(jam, ' '.join(np.char.mod('%d', dividers))))
            J -= 1
        if not J: break
