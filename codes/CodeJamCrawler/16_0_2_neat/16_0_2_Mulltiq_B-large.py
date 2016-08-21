#!/usr/local/env python3.5

import ipdb
import itertools
from sys import stdin


def swap_one(pancake):
    if pancake == '+':
        return '-'
    return '+'


def swap(pancakes):
    return ''.join(swap_one(p) for p in pancakes)[::-1]


def slice_plus(pancakes):
    i = pancakes.rfind('-')
    if i == -1:
        return '', pancakes
    return pancakes[:(i + 1)], pancakes[(i + 1):]


def slice_minus(pancakes):
    i = pancakes.rfind('+')
    if i == -1:
        return '', pancakes
    return pancakes[:(i + 1)], pancakes[(i + 1):]


def main():
    num_cases = int(stdin.readline().strip())
    for i in range(num_cases):
        pancakes = stdin.readline().strip()
        left, _ = slice_plus(pancakes)
        count = 0
        while left != '':
            if left[0] == '-':
                left = swap(left)
                count += 1
                left, _ = slice_plus(left)
            else:
                left, right = slice_minus(left)
                left = swap(left) + right
                count += 1
        print('Case #%s: %s' % (i + 1, count))

if __name__ == '__main__':
    main()
