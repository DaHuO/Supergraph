# coding=utf-8

# Created on <DATE>
# Code Jam <YEAR> <ROUND> <PROBLEM>
# @author: manolo


import sys

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(moves, sign, bottom):

    if len(bottom) == 0:
        if sign == '+':
            return moves
        else:
            return moves + 1

    next = bottom[0]
    bottom = bottom[1:]

    if sign == next:
        return solve(moves, sign, bottom)
    else:
        return solve(moves + 1, next, bottom)


T = int(r())
for case in range(1, T+1):
    line = r()
    if len(line) == 0:
        what = 0
    if len(line) == 1:
        what = 0 if line[0] == '+' else 1
    else:
        what = solve(0, line[0], list(line[1:]))
    w(case, what)


ofile.close


