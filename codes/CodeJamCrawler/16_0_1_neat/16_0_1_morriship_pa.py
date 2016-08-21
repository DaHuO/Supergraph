#!/usr/bin/pypy
# -*- coding: utf-8 -*-
from itertools import imap


def solve():
    n = int(raw_input())
    if not n:
        return 'INSOMNIA'

    result = [0] * 10
    start = 0
    while reduce(lambda x, y: x + y, result, 0) < 10:
        start += n
        for num in imap(int, list(str(start))):
            if not result[num]:
                result[num] = 1
    return start


if __name__ == '__main__':
    output = 'Case #{}: {}'

    t = int(raw_input())
    for i in xrange(1, t + 1):
        print output.format(i, solve())
