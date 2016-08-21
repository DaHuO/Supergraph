#!/usr/bin/pypy
# -*- coding: utf-8 -*-


def solve():
    last = None
    count = 0
    for pancake in (raw_input()):
        if pancake != last:
            last = pancake
            count += 1

    return count - 1 if last == '+' else count


if __name__ == '__main__':
    output = 'Case #{}: {}'

    t = int(raw_input())
    for i in xrange(1, t + 1):
        print output.format(i, solve())
