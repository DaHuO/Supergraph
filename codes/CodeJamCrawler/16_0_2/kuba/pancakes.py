#!/usr/bin/env python
# -*- coding: utf-8 -*-


def flip_pancakes(pancakes):
    flips = 0

    current_side = pancakes[0]

    for pancake in pancakes[1:]:
        if pancake != current_side:
            # flip'em
            flips += 1
            current_side = pancake

    if current_side == '-':
        flips += 1

    return flips


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  pancakes = raw_input()
  print "Case #{0}: {1}".format(i, flip_pancakes(pancakes))
