#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Quals 2016 p.A

    Author: killerrex
"""

import sys
import itertools


def solve(fd):
    """
    Read the cases from fd and solve them

    Args:
        fd: File descriptor

    Returns:
        Number of flips
    """

    total = int(fd.readline().strip())

    for k in range(total):
        # Transform all the consecutive pancakes in a big one
        txt = fd.readline().strip()
        groups = list(c for c, _ in itertools.groupby(txt))

        # We need 2 movements to invert a pancake group deep in the stack
        n = 2*groups.count('-')
        # But just 1 to invert the 1st group
        if groups[0] == '-':
            n -= 1
        print("Case #{}: {}".format(k+1, n))


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)

if __name__ == '__main__':
    start()
