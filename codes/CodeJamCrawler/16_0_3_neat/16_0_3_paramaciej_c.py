#!/usr/bin/env python3

from sys import stderr
from math import ceil

def first_div(n):
    # top = ceil(n**0.5)
    for i in range(2, 500):
        if n % i == 0:
            return i
    return -1

def bases(b, n):
    res = []
    for p in range(2, 11):
        x = 1 + p**(n-1) + p * int(b, p)
        div = first_div(x)
        if div == -1:
            return None
        res.append(div)
    return res

T = int(input())
for t in range(1, T+1):
    N, J = [int(x) for x in input().split()]

    results = []

    for n in range(0, 2 ** (N-2)):
        b = bin(n)[2:]
        r = bases(b, N)
        if r is not None:
            results.append('1' + b.rjust(N-2, '0') + '1 ' + ' '.join([str(x) for x in r]))
        stderr.write("{} / {}\n".format(len(results), b))
        if len(results) >= J:
            break

    print("Case #{}:".format(t))
    for r in results:
        print(r)
