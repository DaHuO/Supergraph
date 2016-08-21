#!/usr/bin/env python

import sys
import copy
from collections import defaultdict

class Case:
    def __init__(self):
        self.N = 0
        self.ans = "INSOMNIA"

    def __repr__(self):
        return "Case-> N: {0}".format(self.N)

    def solve(self):
        if self.N == 0:
            self.ans = "INSOMNIA"
            return

        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        i = 1
        while i < 1000:
            curr = str(self.N * i)
            for d in curr:
                digits.discard(d)

            if len(digits) == 0:
                self.ans = curr
                return

            i += 1
        return

def main(filename):
    cases = readCases(filename)
    i = 1

    for c in cases:
        c.solve()
        print "Case #{0}: {1}".format(i, c.ans)
        i += 1


def readCases(filename):
    cases = []
    with open(filename) as f:
        nbCases = int(f.readline())
        for n in range(nbCases):
            c = Case()
            n = f.readline()
            c.N = int(n)

            cases.append(c)

    # print cases
    assert len(cases) == nbCases
    return cases



if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    main(sys.argv[1])