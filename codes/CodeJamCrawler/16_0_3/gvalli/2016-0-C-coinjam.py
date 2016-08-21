#! /#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys


fh = open(sys.argv[1], 'r')
T = int(fh.readline())  # number of test cases
for t in range(T):
    N, J = [int(a) for a in fh.readline().split()]  # length / num jamcoins

    print('Case #{:d}:'.format(t + 1))
    pattern = '1{:s}1'
    found = 0
    i = 0
    maxpattern = '1' * (N - 2)  # max number to be inside the pattern
    maxnumber = int(maxpattern, base=2)
    while found < J and i <= maxnumber:
        binnumber = bin(i)
        text = binnumber[2:]
        text = ((N - 2) - len(text)) * '0' + text
        number = pattern.format(text)
        divisors = list()
        # print number
        for b in range(2, 10 + 1):
            done = False
            num = int(number, base=b)
            for x in [2] + range(3, int(math.sqrt(num) + 1), 2):
                if num % x == 0:
                    # print number, b, num, x
                    divisors.append(str(x))
                    done = True
                    break
            if not done:
                break  # avoid searching more if on base is prime
        if len(divisors) == 9:
            found += 1
            out = ' '.join(divisors)
            print('{:s} {:s}'.format(number, out))
        # next loop
        i += 1
