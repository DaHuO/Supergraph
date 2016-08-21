#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import math

def divisor(n):
    for i in xrange(2, min(n, 5000)):
        if n % i == 0:
            return i
    return False

with open(argv[1]) as f:
    f.readline()
    case = map(int, f.readline().split())
    heighest = int(math.pow(2, case[0]))
    lowest = heighest/2
    need = int(case[1])
    results = {}
    for i in xrange(lowest, heighest):
        number = format(i, 'b')
        if number[-1] == '0':
            continue
        divisors = list(divisor(int(number, base)) for base in range(2, 11))
        if all(divisors):
            results[number] = divisors
            if len(results) >= need:
                break

    print "Case #1:"
    for jamcoin, results in results.iteritems():
        print jamcoin, " ".join(map(str, results))
