#!/usr/bin/env python
# encoding: utf-8

import sys
import argparse

parser = argparse.ArgumentParser(description="GC")
parser.add_argument('-i', '--in', dest='inFile', required=True,
                    type=argparse.FileType('r'), help='Input file')
parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                    default=sys.stdout, help='Output file (default: stdout)')
args = parser.parse_args()

MINUS = 0
PLUS = 1


def rev(s):
    if s == MINUS:
        return PLUS
    else:
        return MINUS


def flip_until(line):
    rev_sign = rev(line[0])
    for i, c in enumerate(line):
        if c == rev_sign:
            break
        else:
            line[i] = rev_sign
    return line


def flip_all(line):
    for i, c in enumerate(line):
        line[i] = rev(c)
    return line


def flip(line, count):
    nr_minus = sum(x == MINUS for x in line)
    if nr_minus == 0:
        return count
    if nr_minus == len(line):
        return count + 1

    return flip(flip_until(line[:]), count + 1)


def calc(line):
    signs = list(map(lambda x: PLUS if x == '+' else MINUS, line))
    return flip(signs, 0)

header = args.inFile.readline()
nrCases = int(header)
lines = args.inFile.readlines()
for i, line in enumerate(lines):
    assert i < nrCases, "overflow"
    # nrs = list(map(int, line.strip().split(" ")))
    lsg = calc(line.strip())
    print("Case #%d: %s" % (i + 1, lsg), file=args.out)
