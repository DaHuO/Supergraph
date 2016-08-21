#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2016 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,)
#                        unicode_literals)

import itertools
import sys

stdin = sys.stdin
stdout = sys.stdout

# Small Py2/3 compatibility layer
if sys.version_info.major == 2:
    MAXINT = sys.maxint
    MININT = -sys.maxint - 1

    filter = itertools.ifilter
    map = itertools.imap
    range = xrange
    zip = itertools.izip

else:  # >= 3
    MAXINT = sys.maxsize
    MININT = -sys.maxsize - 1


def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


@memodict
def is_prime(n):
    global known_primes
    # for any number ... but the slowest
    # checks diviibility up to the square root of the input
    if n < 2:  # (0, 1)
        return False, 1

    # some known primes
    if n in known_primes:
        return True, 0

    if not (n & 1):  # divisible by 2
        return False, 2

    # Check if divisible by > 3
    for x in range(3, int(pow(n, 0.5)) + 1, 2):
        if not (n % x):
            return False, x

    known_primes.append(n)
    return True, 0


if __name__ == '__main__':
    T = int(stdin.readline())
    N, J = (int(x) for x in stdin.readline().split())

    print('Case #1:')

    j = 0
    for jcoin in itertools.product(range(2), repeat=N - 2):
        jcbases = list()

        for b in range(2, 11):
            bi = pow(b, 0) * 1 + pow(b, N - 1) * 1  # 1st / last bits
            bi += sum(pow(b, N - i - 1) * x for i, x in enumerate(jcoin, 1))
            jcbases.append(bi)

        divisors = list()
        for is_p, divisor in (is_prime(jcb) for jcb in jcbases):
            if is_p:
                break
            divisors.append(divisor)

        if len(divisors) < 9:  # bases 2 -> 10
            continue  # it was prime at some time

        print('1' + ''.join(str(x) for x in jcoin) + '1',
              ' '.join(str(x) for x in divisors))

        j += 1
        if j == J:
            break
