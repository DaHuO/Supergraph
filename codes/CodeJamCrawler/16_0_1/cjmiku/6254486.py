#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import math
import sys

def count(N):
    if N == 0:
        return 'INSOMNIA'
    cutoff = 1000
    i, j = 0, 0
    seen = set()
    while len(seen) < 10:
        i += 1
        n = i * N
        prev = len(seen)
        for d in str(n):
            seen.add(d)
        if j == cutoff:
            break
        j += 1
    if len(seen) < 10:
        return 'INSOMNIA'
    return n

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: %s FILE' % sys.argv[0])
        sys.exit(1)
    fn = sys.argv[1]
    with open(fn) as handle:
        _ = handle.next()
        for i, line in enumerate(handle, start=1):
            line = line.strip()
            if line == "":
                continue
            number = int(line)
            print("Case #%s: %s" % (i, count(number)))
