#!/usr/bin/env python3


def count_flips(pc):
    up = None
    flips = -1
    for p in pc + '+':
        if p != up:
            flips += 1
            up = p
    return flips

for i in range(int(input())):
    pancakes = input()
    print("Case #%s: %s" % (i+1, count_flips(pancakes)))