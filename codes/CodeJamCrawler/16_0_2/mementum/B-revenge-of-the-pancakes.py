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


if __name__ == '__main__':
    T = int(stdin.readline())  # number of testcases
    for case, pcake in enumerate((x.rstrip() for x in stdin), 1):

        turns = 0  # initialize turns counter
        p1 = pcake[0]  # initial position

        for i in range(1, len(pcake)):
            pi = pcake[i]
            if p1 == pi:
                continue  # no need to turn, equal to previous

            # Change .. turn around to get an aligned top
            p1 = pi
            turns += 1  # count the change

        turns += pcake[-1] == '-'  # final turn if needed

        print('Case #%d:' % case, turns)  # output
