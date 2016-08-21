#!/usr/bin/env python3
import os.path
import sys


def solve(S):
    if S == '':
        return 0
    pre, sep, post = S.rpartition('-')
    S = pre + sep
    if S == '':    # all are happy
        return 0
    if S[0] == '-':
        return solve(rev(S)) + 1

    pre, sep, post = S.partition('-')
    return solve(rev(pre) + sep + post) + 1


def rev(stack):
    new = ''
    for ch in reversed(list(stack)):
        if ch == '+':
            new += '-'
        else:
            new += '+'
    return new


# main
me = sys.argv[0].split("/")[-1].replace(".py", "")
# file = me + "-sample"
# file = me + "-small-attempt0"
file = me + "-large"

infile = file + ".in"
if not os.path.exists(infile):
    infile += ".txt"

with open(infile, "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            S = fdin.readline()

            result = solve(S)

            line = "Case #%d: %s" % (ncase + 1, result)
            print(line)
            fdout.write("%s\n" % line)
