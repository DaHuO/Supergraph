# -*- coding: utf-8 -*-

"""\

┻┻︵⁞=༎ຶ﹏༎ຶ=⁞︵┻┻

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a
single integer N, the number Bleatrix has chosen.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y
is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.

Limits

1 ≤ T ≤ 100.

"""

from __future__ import unicode_literals
from __future__ import print_function

import argparse
from collections import defaultdict


def readl(f):
    return f.next().strip()


def process(n):
    if n == 0:
        return 'INSOMNIA'
    seen = set()
    j = 1
    while True:
        next = n * j
        seen.update(list(str(next)))
        if len(seen) == 10:
            return next
        j += 1


def output_results(results, f):
    for i, res in enumerate(results):
        print("Case #%s: %s" % (i + 1, res), file=f)


def solve(f):
    test_cases = readl(f)
    results = []
    try:
        while True:
            n = readl(f)
            results.append(process(int(n)))
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
        x = solve(f)
    with open(args.output, 'w') as f:
        output_results(x, f)


if __name__ == '__main__':
    main()
