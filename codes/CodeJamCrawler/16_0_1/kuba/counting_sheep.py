#!/usr/bin/env python
# -*- coding: utf-8 -*-


def still_counting(digits):
    return 10 != len(digits)


def digitize(n):
    yield n % 10
    n /= 10

    while n:
        yield n % 10
        n /= 10


def update_digits(n, digits):
    for digit in digitize(n):
        digits.add(digit)


def sleep_bleatrix(n):
    if 0 == n:
        return 'INSOMNIA'

    digits = set()

    m = n
    update_digits(m, digits)

    while still_counting(digits):
        m += n
        update_digits(m, digits)

    return m


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())
  print "Case #{0}: {1}".format(i, sleep_bleatrix(n))
