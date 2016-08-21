#! /#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys


def get_number(coords, length):
    val = 1
    N = len(coords)
    for i in range(N):
        # print length, '^', (N - 1) - i, '*', coords[i] - 1
        val += (length ** ((N - 1) - i)) * (coords[i] - 1)
    return val

# print get_number([1, 2, 3], 4)
# print get_number([1, 2, 4], 4)
# exit(0)

fh = open(sys.argv[1], 'r')
T = int(fh.readline())  # number of test cases
for t in range(T):
    K, C, S = [int(a) for a in fh.readline().split()]  # length / comp / grad

    # Minimum number to get all
    if C > 1:
        minimum = int(math.ceil(K / float(C - 1)))
    else:
        minimum = K

    # Impossible or possible
    if S < minimum:
        # Impossible
        print('Case #{:d}: IMPOSSIBLE'.format(t + 1))
    else:
        # Possible
        allindexs = set(range(1, K + 1))
        numtouse = C
        coordinates = list()
        currentindexs = set(range(1, K + 1))
        for s in range(S):
            indextouse = set()
            if len(currentindexs) >= numtouse:
                # get the ones you want
                for a in range(numtouse):
                    indextouse.add(currentindexs.pop())
                indextouse = list(indextouse)
            else:
                # fill with already used indexes
                indextouse = [1] * (numtouse - len(currentindexs))
                indextouse += list(currentindexs)

            # get location in the final tiles (which to clean)
            num = get_number(indextouse, K)
            coordinates.append(str(num))
            currentindexs -= set(indextouse)
            # Finish condition
            if len(currentindexs) == 0:
                res = ' '.join(coordinates)
                print('Case #{:d}: {:s}'.format(t + 1, res))
                break
