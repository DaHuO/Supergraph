#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys


def calculate_last_number(_N):
    if _N == 0:
        return "INSOMNIA"

    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    i = 0
    while len(digits) > 0:
        i += 1
        _M = _N * i
        for digit in str(_M):
            if digit in digits:
                digits.remove(digit)

    return _N * i


def main():
    _T = int(raw_input())
    for t in range(_T):
        _N = int(raw_input())
        result = calculate_last_number(_N)
        print "Case #{0}: {1}".format(t + 1, result)


if __name__ == '__main__':
    main()
