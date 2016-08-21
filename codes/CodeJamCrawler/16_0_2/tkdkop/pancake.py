#!/usr/bin/env python
import sys
import itertools


m = sys.stdin.readline()
i = 0
for line in sys.stdin.readlines():
    line = line.strip()
    i += 1
    out_str = "Case #%d: " % i

    line += '+'
    k = itertools.groupby(line)
    out_str += str(len(list(k))-1)
    print out_str
