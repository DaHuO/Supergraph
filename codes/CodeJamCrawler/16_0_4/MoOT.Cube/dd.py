#!/usr/bin/env python

import sys
import itertools
import math

if __name__ == "__main__":
    for (i, l) in enumerate([l.rstrip("\n") for l in sys.stdin.readlines()[1:]]):
        (k,c,s) = map(int, l.split(" "))
        kk = range(k)
        if s*c >= k:
            kki = [itertools.islice(itertools.cycle(kk), 0, math.ceil(k/c)*c)] * c
            tiles = list(map(lambda x: list(filter(lambda x: x != None, x)), itertools.zip_longest(*kki)))
            solution = [1+sum(map(lambda x: x[1]*(k**x[0]), enumerate(l))) for l in tiles]
            print("Case #" + str(i + 1) + ": " + " ".join(map(str, solution)))
        else:
            print("Case #" + str(i + 1) + ": " + "IMPOSSIBLE")
