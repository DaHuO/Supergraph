#!/usr/bin/env python

import numpy as np
import sys

def flip(sequence):
    flipped = list(sequence)
    totalLength = len(sequence)
    for ik in np.arange(totalLength):
        if sequence[ik] == '+':
            flipped[totalLength - 1 - ik] = '-'
        elif sequence[ik] == '-':
            flipped[totalLength - 1 - ik] = '+'
    return flipped


def turn(sequence):
    turned = list(sequence)
    totalLength = len(sequence)
    for ik in np.arange(totalLength):
        if sequence[ik] == '+':
            turned[ik] = '-'
        elif sequence[ik] == '-':
            turned[ik] = '+'
    return turned


def flip_count(pancakes):
    count = 0
    pancakes = list(pancakes)
    if len(pancakes) == 1:
        if pancakes[0] == '+':
            count = 0
        else:
            count = 1
    elif len(pancakes) >= 2:
        if pancakes[-1] == '+':
            count = flip_count(pancakes[0:-1])
        elif (pancakes[-1] == '-') & (pancakes[0] == '-'):
            count = 1 + flip_count(flip(pancakes))
        elif (pancakes[-1] == '-') & (pancakes[0] == '+'):
            count = 1 + flip_count(turn(pancakes))

    return count


# Main Function ...

filename = sys.argv[1]
f = open(filename)
nround = np.int(f.readline())
iround = 0

for line in f.readlines():
    iround += 1
    sequence = line.split()[0]
    nflip = flip_count(sequence)
    print "\nCase #{0}: {1}".format(iround, nflip)
