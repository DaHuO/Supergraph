#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Quals 2016 p.A
  
    Author: killerrex
"""

import sys


def as_number(fd, kind=int, single=False):
    """
    Read one line from the file and return it
    as the required kind numbers

    Args:
        fd: File descriptor
        kind: A transformation function like int, float...
        single: Return a single number

    Returns:
        The list/single values
    """

    txt = fd.readline().strip()
    values = [kind(s) for s in txt.split()]
    if single:
        if values:
            return values[0]
        else:
            return None
    else:
        return values


# Brute force
def counting(n):
    """

    Args:
        n: first number

    Returns: The number searched or INSOMNIA

    """

    # Only non-stop condition
    # Otherwise no matter the initial number, the MSD will cover all,
    # sooner or later
    if n == 0:
        return 'INSOMNIA'

    s = set()
    res = 0
    while len(s) < 10:
        res += n
        s |= set(str(res))
    return res


def solve(fd):
    """
    Solve for the values from a file

    Args:
        fd: File unit
    """
    # First line is the number of cases
    total = as_number(fd, single=True)

    for k in range(total):
        n = as_number(fd, single=True)
        print("Case #{}: {}".format(k+1, counting(n)))


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)

if __name__ == '__main__':
    start()
