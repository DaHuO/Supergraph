#!/usr/bin/env python3
"""
Problem B. Revenge of the Pancakes
CodeJam 2016: Qualification Round
https://code.google.com/codejam/contest/6254486/dashboard

Example of how to run:
$ ./pancake_revenge.py < sample.in > sample.out

Validate:
$ diff -s sample.out sample.out.key
Files sample.out and sample.out.key are identical
"""
import re

__author__ = "Tatiana Al-Chueyr"
__email__ = "tatiana.alchueyr@gmail.com"
__date__ = "2016-04-09"
__version__ = "1.0.0"


is_negative = lambda chunk: chunk.startswith("-")


def split_pancakes_by_type(pancake_stack):
    """
    Given a string containing a pancake stack, split it into chunks based on
    the happiness of the pancake.

    Example:
        >>> split_pancakes("+-++--+++-")
        ['+', '-', '++', '--', '+++', '-']
    """
    return [m.group(0) for m in re.finditer(r"([\+\-])\1*", pancake_stack)]


def solve(pancake_stack):
    """
    Compute the minimum number of times we need to execute the pancake flipping
    manewver to get all the pancakes happy side up.

    Example:
        >>> solve("-+")
        1
    """
    chunks = split_pancakes_by_type(pancake_stack)
    total_flips = len(chunks) - 1
    if is_negative(chunks[-1]):
        total_flips += 1
    return total_flips


if __name__ == "__main__":
    TOTAL = int(input())
    for i in range(1, TOTAL + 1):
        pancake_stack = input()
        print("Case #{}: {}".format(i, solve(pancake_stack)))
