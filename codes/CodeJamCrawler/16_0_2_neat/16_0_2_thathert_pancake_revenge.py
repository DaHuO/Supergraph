# -*- coding: utf-8 -*-

"""\

┻┻︵⁞=༎ຶ﹏༎ຶ=⁞︵┻┻

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a
string S, each character of which is either + (which represents a pancake that is initially happy side up) or - (which
represents a pancake that is initially blank side up). The string, when read left to right, represents the stack when
viewed from top to bottom.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is
the minimum number of times you will need to execute the maneuver to get all the pancakes happy side up.


"""

from __future__ import print_function

import argparse
from collections import defaultdict


TEST_OUT = 'data/debug.txt'


def readl(f):
    return f.next().strip()


def swap(seq, h, t):
    while (t - 1) > h:
        tmp = seq[h]
        seq[h] = seq[t - 1]
        seq[t - 1] = tmp
        t -= 1
        h += 1


def in_flip(seq, h, t, debug=None):
    for i in range(t):
        if seq[i + h] == '-':
            seq[i + h] = '+'
        else:
            seq[i + h] = '-'
    swap(seq, h, t)
    if debug is not None:
        print(''.join(seq), file=debug)


def flip(seq, tail_idx, debug=None):
    # take in all the items at the head that are the same
    flip_ops = 0
    item_ = seq[0]
    j = 1
    while j < len(seq) and seq[j] == item_:
        j += 1
    if seq[0] == '+':
        flip_ops += 1
        in_flip(seq, 0, j, debug=debug)
    # find the real number of leading - now
    leading_minus = 0
    while leading_minus < len(seq) and seq[leading_minus] == '-':
       leading_minus += 1
    in_flip(seq, 0, tail_idx + 1, debug=debug)  # used as range counter instead of index
    flip_ops += 1
    return leading_minus, flip_ops


def process(seq, debug=None):
    if seq == '-':
        return 1
    elif seq == '+':
        return 0
    seq = list(seq)
    tail_idx = len(seq) - 1
    # start by seeing whether we can decrement the tail_idx from the outset
    while tail_idx >= 0 and seq[tail_idx] == '+':
        tail_idx -= 1
    flipped_ops = 0
    while tail_idx >= 0 and '-' in seq:
        flipped_count, flip_ops = flip(seq, tail_idx, debug=debug)
        flipped_ops += flip_ops
        tail_idx -= flipped_count
    return flipped_ops


def output_results(results, f):
    for i, res in enumerate(results):
        print("Case #%s: %s" % (i + 1, res), file=f)


def solve(f, debug=None):
    test_cases = readl(f)
    results = []
    try:
        while True:
            seq = readl(f)
            results.append(process(seq, debug=debug))
    except StopIteration:
        pass
    return results


def main():
    # TODO: fix positional args
    parser = argparse.ArgumentParser(description='The prices are mixed!')
    parser.add_argument('file', type=str, help='the input', default='./data/in')
    parser.add_argument('output', type=str, help='the output', default='./data/out')
    args = parser.parse_args()
    with open(args.file) as f:
        with open(TEST_OUT, 'w') as debug:
            x = solve(f, debug=debug)
    with open(args.output, 'w') as f:
        output_results(x, f)


if __name__ == '__main__':
    main()
