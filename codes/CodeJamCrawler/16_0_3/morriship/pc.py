#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from math import sqrt
from itertools import imap

import numpy


# Copy from stackoverflow, link: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


def convert_base(num, raw_base, new_base):
    x = 1
    result = 0
    while num:
        result += (num % new_base) * x
        x *= raw_base
        num //= new_base
    return result


def calc(num):
    result = [num]
    for i in xrange(2, 11):
        value = convert_base(num, i, 10)
        limit = sqrt(value) + 1
        divisor = 0
        for prime in primes:
            if prime > limit:
                break
            if value % prime == 0:
                divisor = value / prime
                break
        result.append(divisor)

    return (all(result), result)


def solve():
    n, j = map(int, raw_input().split())
    start = 2 ** (n - 1) + 1
    result = []
    while len(result) < j:
        is_valid, ans = calc(convert_base(start, 10, 2))
        if is_valid:
            result.append(map(str, ans))
        start += 2
    result = imap(' '.join, result)
    return '\n' + '\n'.join(result)


if __name__ == '__main__':
    output = 'Case #{}:{}'
    primes = primesfrom2to(2 ** 16)

    t = int(raw_input())
    for i in xrange(1, t + 1):
        print output.format(i, solve())
