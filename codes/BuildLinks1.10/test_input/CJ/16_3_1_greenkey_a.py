#! /usr/bin/env python

import sys
from collections import OrderedDict
from operator import itemgetter


class GoogleCodeJamHelper:
    def __init__(self, inputFileName):
        self.f = open(inputFileName, 'r')

    def readInt(self):
        return int(self.f.readline().strip())

    def readInts(self):
        return [int(x) for x in self.f.readline().strip().split(sep=" ")]

    def readStr(self):
        return self.f.readline().strip()

    def readStrs(self):
        return self.f.readline().strip().split(' ')


def dprint(s):
    """Debug Print, it prints on the stderr"""
    print(s, file=sys.stderr)


def solve(ns):
    dprint(ns)
    d = dict()
    exits = ""
    for i in range(len(ns)):
        d[chr(65+i)] = ns[i]
    dprint(d)
    while sum(d.values()) > 0:
        s = sorted(d.items(),key=lambda x: x[1], reverse=True)
        b1 = s[0][0]
        b2 = s[1][0]
        dprint(s)
        if d[b2] > 0:
            exits = b1 + b2 + ' ' + exits
            d[b1] -= 1
            d[b2] -= 1
        else:
            exits = b1 + ' ' + exits
            d[b1] -= 1
    return exits.strip()



gc = GoogleCodeJamHelper(sys.argv[1])

for i in range(gc.readInt()):
    dprint("\n===Case {}".format(i + 1))
    gc.readInt()
    print("Case #{}: {}".format(i + 1, solve(gc.readInts())))
