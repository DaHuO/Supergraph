#!/usr/bin/env python3
import sys


def solve(N):
    if N == 0:
        return "INSOMNIA"

    i = 1
    seen = set()
    while True:  # XXX
        n = i * N
        seen = seen.union(set(str(n)))
        # print(n, seen)
        if len(seen) == 10:
            return n
        i += 1

    return "INSOMNIA"


# main
me = sys.argv[0].split("/")[-1].replace(".py", "")
# file = me + "-sample"
# file = me + "-small-attempt0"
file = me + "-large"

with open(file + ".in.txt", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            N = int(fdin.readline())

            result = solve(N)

            line = "Case #%d: %s" % (ncase + 1, result)
            print(line)
            fdout.write("%s\n" % line)
