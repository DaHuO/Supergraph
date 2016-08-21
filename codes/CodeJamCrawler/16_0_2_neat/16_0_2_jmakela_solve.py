# -*- coding: utf-8 -*-
# Copyright (c) 2016 Jonathan Makela <socillion@gmail.com>

from __future__ import print_function

"""
Problem

The Infinite House of Pancakes has just introduced a new kind of pancake! It
has a happy face made of chocolate chips on one side (the "happy side"), and
nothing on the other side (the "blank side").

You are the head waiter on duty, and the kitchen has just given you a stack of
pancakes to serve to a customer. Like any good pancake server, you have X-ray
pancake vision, and you can see whether each pancake in the stack has the happy
side up or the blank side up. You think the customer will be happiest if every
pancake is happy side up when you serve them.

You know the following maneuver: carefully lift up some number of pancakes
(possibly all of them) from the top of the stack, flip that entire group over,
and then put the group back down on top of any pancakes that you did not lift
up. When flipping a group of pancakes, you flip the entire group in one motion;
you do not individually flip each pancake. Formally: if we number the pancakes
1, 2, ..., N from top to bottom, you choose the top i pancakes to flip. Then,
after the flip, the stack is i, i-1, ..., 2, 1, i+1, i+2, ..., N.
Pancakes 1, 2, ..., i now have the opposite side up, whereas
pancakes i+1, i+2, ..., N have the same side up that they had up before.

For example, let's denote the happy side as + and the blank side as -. Suppose
that the stack, starting from the top, is --+-. One valid way to execute the
maneuver would be to pick up the top three, flip the entire group, and put
them back down on the remaining fourth pancake (which would stay where it is
and remain unchanged). The new state of the stack would then be -++-. The other
valid ways would be to pick up and flip the top one, the top two, or all four.
It would not be valid to choose and flip the middle two or the bottom one, for
example; you can only take some number off the top.

You will not serve the customer until every pancake is happy side up, but you
don't want the pancakes to get cold, so you have to act fast! What is the
smallest number of times you will need to execute the maneuver to get all
the pancakes happy side up, if you make optimal choices?

Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each consists of one line with a string S, each character of which is
either + (which represents a pancake that is initially happy side up) or -
(which represents a pancake that is initially blank side up). The string, when
read left to right, represents the stack when viewed from top to bottom.

Output

For each test case, output one line containing Case #x: y, where x is the test
case number (starting from 1) and y is the minimum number of times you will
need to execute the maneuver to get all the pancakes happy side up.

Limits

1 ≤ T ≤ 100.
Every character in S is either + or -.

###################################################
Need all +s in string. Can 'flip' part, reversing string and swapping +/-s.
Result - min number for all +s.

case: +-++
case: +---+---+-
case: +++-++
case: +-+-+-

Need to 'erase' 'pockets' of -s.
1. If top of stack is -, convert all contiguous to +.
2. If top if stack is + and - is present, flip everything up to last
    contiguous - stretch. If result is same, flip 1 less.
"""


def read_all_cases(filename, case_reader):
    with open(filename) as f:
        count = int(f.readline())
        cases = []
        for _ in xrange(count):
            cases.append(case_reader(f))
        return cases


def output_results(results, f):
    for x, r in enumerate(results):
        print("Case #{}: {}".format(x+1, r), file=f)


def test_run(case_reader, run_case, infile, outfile):
    import StringIO

    cases = read_all_cases(infile, case_reader)
    results = map(run_case, cases)
    buf = StringIO.StringIO()
    output_results(results, buf)
    got = buf.getvalue().splitlines()

    with open(outfile) as f:
        expected = [ln.strip() for ln in f.readlines()]

    wrong = 0
    for g, e in zip(got, expected):
        if g != e:
            print("Got '{}', expected '{}'".format(g.strip(), e.strip()))
            wrong += 1
    if not wrong:
        print("Sample: all correct.")


def live_run(case_reader, run_case, infile, outfile):
    cases = read_all_cases(infile, case_reader)
    results = map(run_case, cases)
    with open(outfile, 'w') as f:
        output_results(results, f)
    print("Live run: Done.")


################################################################################
################################################################################
################################################################################


def read_case(f):
    return f.readline().strip()


def flip(n, s):
    """n: number to flip. s: stack of pancakes."""
    # print("flipped {} of {}".format(n, s))
    flipped = s[:n][::-1]
    ret = []
    for x in flipped:
        if x == '+':
            ret += '-'
        else:
            ret += '+'
    return ''.join(ret) + s[n:]


def solve_case(stack):
    print("Solving {}".format(stack))
    flips = 0

    while '-' in stack:
        idx = -1
        if stack.startswith('-'):
            idx = stack.find("+")
            if idx == -1:
                idx = len(stack)
        else:
            # find last stretch of '-'*n in stack, flip everything before that
            idx = stack.rfind('-')
            while stack[idx-1] == '-':
                idx -= 1
        stack = flip(idx, stack)
        flips += 1
    return flips


def main():
    import sys
    if len(sys.argv) >= 2:
        fname = sys.argv[1]
        infile = fname + '.in'
        outfile = fname + '.out'
        live_run(read_case, solve_case, infile, outfile)
    else:
        test_run(read_case, solve_case, 'sample.in', 'sample.out')


if __name__ == '__main__':
    main()
