#!/usr/bin/env python3

import sys


def flip(cakes, n=None, count=0):
    if n != None:
        count += 1
        x = 0
        while x < n:
            cakes[x] = ('+' if cakes[x] == '-' else '-')
            x += 1
    for (i, c) in enumerate(cakes[::-1]):
        if c == '-':
            return flip(cakes, len(cakes) - i, count)
    return count


if __name__ == '__main__':
    for (i, cakes) in enumerate(sys.stdin):
        if i == 0:
            continue
        print('Case #' + str(i) + ': ' + str(flip(list(cakes.strip()))))
