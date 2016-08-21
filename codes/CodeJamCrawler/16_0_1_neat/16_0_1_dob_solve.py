#!/usr/bin/env python
from __future__ import print_function
import sys
import time
from functools import reduce

if '-d' in sys.argv[1:]:
    def dbg(*args):
        print(*args)
        sys.stdout.flush()
else:
    def dbg(*args):
        pass

def readline():
    return sys.stdin.readline().strip()

def readfloat():
    return float(readline())

def readfloats():
    return [float(x) for x in readline().split()]

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().split()]

def solve_case():
    N = readint()
    if not N:
        return 'INSOMNIA'
    N0 = N
    digits = set(str(N))
    while True:
        if len(digits) == 10:
            return N
        N += N0
        digits |= set(str(N))

def main():
    cases = readint()
    for c in range(1, cases + 1):
        t0 = time.time()
        print('Case #{0:d}: {1}'.format(c, solve_case()))
        #dbg('{:.6f}'.format(time.time() - t0))

if __name__ == '__main__':
    main()

