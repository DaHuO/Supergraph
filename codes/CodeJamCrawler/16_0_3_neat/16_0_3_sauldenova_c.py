#!/usr/local/bin/python3

from __future__ import print_function
from math import sqrt, ceil
from subprocess import call

T = int(input())
N, J = [int(a) for a in input().split(' ')]
numberCount = 0

print('Case #1:')
results = [0 for i in range(11)]

for i in range(0, 2**(N - 2)):
    number = '1' + '{0:0{width}b}'.format(i, width=(N - 2)) + '1'
    is_valid = True
    for base in range(2, 11):
        results[base] = 0
        num = int(number, base=base)
        for numba in range(2, int(ceil(sqrt(num)))):
            if num % numba == 0:
                results[base] = numba
                break

        if results[base] == 0:
            is_valid = False
            break

    if is_valid:
        print(number, end='')
        for base in range(2, 11):
            print(' ', results[base], sep='', end='')
        print()
        numberCount += 1

    if numberCount >= J:
        break

