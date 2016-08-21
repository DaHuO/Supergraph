#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def solver(pancake):
    iter = 0
    position = 1
    while True:
        if sum(pancake) == pancake.size:
            break
        if sum(pancake) == 0:
            flip(pancake, position)
            iter += 1
            break
        if pancake[position-1] != pancake[position]:
            flip(pancake, position)
            iter += 1
        position += 1
    return iter


def flip(pancake, ith):
    assert ith <= pancake.size
    pancake[:ith] = ~pancake[:ith]
    return pancake


def convert_pancakes(pancake_str):

    pancake = np.zeros(len(pancake_str), np.bool)
    for i in xrange(len(pancake_str)):
        if pancake_str[i] == '-':
            pancake[i] = False
        else:
            pancake[i] = True
    return pancake


if __name__ == "__main__":

    testcases = input()

    for caseNr in xrange(1, testcases+1):
        pancakes_str = raw_input()
        pancake = convert_pancakes(pancakes_str)
        nflip = solver(pancake)
        print "Case #%i: %s" % (caseNr, nflip)