#!/usr/bin/python
#
# Google Code Jam Round 1 - problem A
#   16.04.2016
#
# Author:
#   Liviu Chircu <liviu.chircu@gmail.com>

import sys

def solve(nfi):
    with open(nfi, 'r') as fi:
        with open(nfi.replace("in", "out"), "a") as fo:
            fo.truncate(0)
            T = int(fi.readline())

            for case in xrange(1, T+1):
                S = fi.readline().split()[0]

                W = S[0]
                for let in S[1:]:
                    if let < W[0]:
                        W = W + let
                    else:
                        W = let + W

                fo.write("Case #{}: {}\n".format(case, W))

solve(sys.argv[1])
