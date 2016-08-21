#!/usr/bin/env python
# -*- coding: utf-8 -*-


def flip(a, i, j):
    b = [val for val in a]
    for w in range(i, j + 1):
        b[j - w + i] = 1 - a[w]
    return b


def solve(line):
    a = [0 for i in line]
    for i in range(0, len(line)):
        if line[i] == '+':
            a[i] = 1

    count = 0
    pos = len(a) - 1
    while pos >= 0:
        if a[pos] == 0:
            if a[0] == 0:
                a = flip(a, 0, pos)
                count = count + 1
            else:
                i = pos
                while a[i] != 1 and i >= 0:
                    i = i - 1
                a = flip(a, 0, i)
                a = flip(a, 0, pos)
                count = count + 2
        pos = pos - 1
    return count


if __name__ == "__main__":
    testcases = input()
         
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
