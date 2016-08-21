#!/usr/bin/env python

import math
import fileinput

def remove(s, ds):
    for d in ds:
        s = s.replace(d, '', 1)
    return s

def resolve(s):
    digits = []
    uniques = [
        ('Z', 0, 'ZERO'),
        ('W', 2, 'TWO'),
        ('U', 4, 'FOUR'),
        ('X', 6, 'SIX'),
        ('G', 8, 'EIGHT'),
        ('O', 1, 'ONE'),
        ('H', 3, 'THREE'),
        ('S', 7, 'SEVEN'),
        ('F', 5, 'FIVE'),
        ('N', 9, 'NINE'),
    ]
    for c, v, ds in uniques:
        while c in s:
            digits.append(v)
            s = remove(s, ds)

    assert len(s) == 0

    digits.sort()
    return ''.join(str(d) for d in digits)

if __name__ == "__main__":
    input = fileinput.input()
    nbtst = int(input.readline())
    for idx in range(nbtst):
        print 'Case #{}: {}'.format(idx+1, resolve(input.readline().strip()))
