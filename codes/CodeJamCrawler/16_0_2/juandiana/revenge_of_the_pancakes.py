#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys


def flip(s):
    return ''.join(map(lambda c: '+' if c == '-' else '-', s))


def perform_maneuver(top_part):
    if len(top_part) == 1:
        return flip(top_part)

    if top_part[0] == '+':
        i = 0
        while top_part[i] == '+':
            i += 1
        return flip(top_part[:i]) + top_part[i:]
    else:
        return ''.join(map(lambda x: flip(x), top_part[::-1]))


def calculate_min_number_of_maneuvers(_S):
    maneuvers = 0

    i = len(_S) - 1
    while i >= 0:
        if _S[i] == '+':
            i -= 1
        else:  # _S[i] == '-'
            top_part = _S[:i] + _S[i]
            bottom_part = _S[i + 1:]
            _S = perform_maneuver(top_part) + bottom_part
            maneuvers += 1

    return maneuvers


def main():
    _T = int(raw_input())
    for t in range(_T):
        _S = str(raw_input())
        result = calculate_min_number_of_maneuvers(_S)
        print "Case #{0}: {1}".format(t + 1, result)


if __name__ == '__main__':
    main()
