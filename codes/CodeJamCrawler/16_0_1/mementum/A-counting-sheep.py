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


def solve(N):
    digits = dict()

    for n in (N * i for i in itertools.count(1)):
        n2 = n
        while n2:
            digits[n2 % 10] = 1
            n2 //= 10

        if len(digits) == 10:
            break

    return n


def result(i, res):
    print('Case #%d:' % i, res)


if __name__ == '__main__':
    N = int(stdin.readline())
    for case, N in enumerate((int(x) for x in stdin), 1):
        if not N:
            result(case, 'INSOMNIA')
            continue

        result(case, solve(N))
