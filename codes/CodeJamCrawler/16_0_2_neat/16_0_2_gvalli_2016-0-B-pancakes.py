#! /#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

flip = {'+': '-', '-': '+'}

fh = open(sys.argv[1], 'r')
T = int(fh.readline())  # number of test cases
for t in range(T):
    S = fh.readline().split()[0]  # position of each pancake + - top to bottom
    flips = 0
    done = False
    # print ''
    # print S
    while not done:
        # Check finished
        done = True
        for c in S:
            # print 'check', c
            if c == '-':
                done = False
                break
        # Flip from the back
        if not done:
            # print len(S)
            last = S[-1]
            i = len(S) - 1
            while S[i] == last and i >= 0:
                # print i
                i -= 1
            i += 1  # real index
            # all equal to -, flip all
            if i == 0:
                i = len(S)
            toflip = S[:max(i, 1)]
            # print 'to', toflip, i
            flipped = ''
            for c in toflip:
                flipped += flip[c]
            S = flipped + S[max(i, 1):]
            flips += 1
            # print S
            # raw_input('>')

    print('Case #{:d}: {:d}'.format(t + 1, flips))
