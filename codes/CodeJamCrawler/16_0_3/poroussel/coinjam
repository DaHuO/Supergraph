#!/usr/bin/env python

import math
import fileinput

pows = {}

ump = []

def add(bits):
    nbits = [d for d in bits]
    for pos in range(1, len(bits)):
        if nbits[pos] == 0:
            nbits[pos] = 1
            return nbits
        nbits[pos] = 0
    return nbits

def resolve(n, j):
    res = []

    bits = [0] * n
    bits[0] = 1
    bits[-1] = 1

    while len(res) < j:
        divisors = []
        for b in range(2, 11):
            val = sum(pows[b][idx] * digit for idx, digit in enumerate(bits))
            if not val in ump:
                found = False
                for d in xrange(2, 10000):
                    if val % d == 0:
                        divisors.append(d)
                        found = True
                        break
                if not found:
                    ump.append(val)
        if len(divisors) == 9:
            res.append((bits, divisors))
        bits = add(bits)
    return res


if __name__ == "__main__":
    for b in range(2, 11):
        pows[b] = [pow(b, p) for p in range(0, 33)]

    input = fileinput.input()
    nbtst = int(input.readline())
    for idx in range(nbtst):
        val = [int(v) for v in input.readline().split()]
        print 'Case #{}:'.format(idx+1)
        for jc in resolve(val[0], val[1]):
            bits = jc[0]
            bits.reverse()
            print ''.join(str(b) for b in bits), ' '.join(str(d) for d in jc[1])
