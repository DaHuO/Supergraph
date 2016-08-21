#!/usr/bin/env python3

import sys

filename = sys.argv[1]
num_cases = 0


def reverse_first_n(sides, n):
    for i in range(0, n):
        sides[i] = not sides[i]
    return sides

def count_lifts(sides):
    count = 0
    for i in range(len(sides), 0, -1):
        if not sides[i - 1]:
            sides = reverse_first_n(sides, i)
            count = count + 1
    return count

def min_lifts(sides):
    happy_sides = []
    for c in sides:
        if c == '+':
            happy_sides.append(True)
        else:
            happy_sides.append(False)
    return count_lifts(happy_sides)

with open(filename, 'r') as f:
    num_cases = int(f.readline().strip())
    for i in range(1, num_cases + 1):
        lifts = min_lifts(f.readline().strip())
        print("Case #%d: %s" % (i, lifts))

