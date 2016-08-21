#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys


def read(f):
    N = int(f.readline())
    inputs = [line.strip() for line in f]
    assert len(inputs) == N
    return inputs


def split(s):
    return [x for x in s.split('+') if x]


def solve(s):
    xs = split(s)
    return 2 * len(xs) - (1 if s.startswith('-') else 0)


def main():
    inputs = read(sys.stdin)
    for i, s in enumerate(inputs, start=1):
        print('Case #{}: {}'.format(i, solve(s)))


if __name__ == '__main__':
    main()
    
