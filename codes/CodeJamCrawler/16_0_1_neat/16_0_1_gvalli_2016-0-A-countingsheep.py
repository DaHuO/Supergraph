#! /#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

fh = open(sys.argv[1], 'r')
T = int(fh.readline())  # number of test cases
for t in range(T):
    N = int(fh.readline())  # starting number
    done = list()  # numbers already processed, detect loops
    numbers = list()  # digits encountered
    sleep = False  # termination condition
    i = 1  # multiplying index
    # print N
    while not sleep:
        curr = i * N  # current number
        text = str(curr)  # get current in text
        # print curr, i
        for c in text:
            if c not in numbers:
                numbers.append(c)  # save each new digit
        # print numbers
        if len(numbers) == 10:
            # all digits seen
            sleep = True
            res = curr
        if curr in done:
            # detected a loop
            sleep = True
            res = 'INSOMNIA'
        done.append(curr)
        # next loop
        i += 1

    print('Case #{:d}: {}'.format(t + 1, res))
