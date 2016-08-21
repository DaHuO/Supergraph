#!/usr/bin/env python
# encoding: utf-8

import sys
import argparse
import itertools

parser = argparse.ArgumentParser(description="GC")
parser.add_argument('-i', '--in', dest='inFile', required=True,
                    type=argparse.FileType('r'), help='Input file')
parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                    default=sys.stdout, help='Output file (default: stdout)')
args = parser.parse_args()

bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]


from math import sqrt
from functools import lru_cache, reduce
from collections import Counter
from itertools import product

MUL = int.__mul__

def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)

@lru_cache(maxsize=None)
def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]

@lru_cache(maxsize=None)
def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    try:
        divs.remove(1)
    except KeyError:
        pass

    return divs


def calc(ns, out):
    n, j = ns
    i = 0
    for p in itertools.product([0, 1], repeat=n - 2):
        p = list(p)
        p.insert(0, 1)
        p.append(1)

        ps = ''.join(map(str, p))
        divs = []
        for b in bases:
            bs = int(ps, b)
            ds = proper_divs(bs)
            if len(ds) == 0:
                break
            divs.append(ds.pop())

        if len(divs) == 9:
            print(ps, file=out, end=' ')
            print(' '.join(map(str, divs)), file=out)
            i += 1

        if i >= j:
            break

header = args.inFile.readline()
nrCases = int(header)
lines = args.inFile.readlines()
for i, line in enumerate(lines):
    assert i < nrCases, "overflow"
    nrs = list(map(int, line.strip().split(" ")))
    print("Case #%d:" % (i + 1))
    calc(nrs, args.out)
