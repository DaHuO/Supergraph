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


def calc(n):
    if n == 0:
        return "INSOMNIA"
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 1
    while i < 10000:
        ts = i * n
        for t in str(ts):
            if t in digits:
                digits.remove(t)
        if len(digits) == 0:
            return ts
        i += 1
    return "INSOMNIA"

header = args.inFile.readline()
nrCases = int(header)
lines = args.inFile.readlines()
for i, line in enumerate(lines):
    assert i < nrCases, "overflow"
    # nrs = list(map(int, line.strip().split(" ")))
    nr = int(line.strip())
    lsg = calc(nr)
    print("Case #%d: %s" % (i + 1, lsg), file=args.out)
