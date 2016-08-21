#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from codejam.common import CodeJamIO, Problem, ProblemInstance


#===============================================================================
# Store credit problem
#===============================================================================

class CountSheeps(ProblemInstance):

    def __init__(self):
        self.n = CodeJamIO.read_int()

    def solve(self):
        if self.n == 0:
            return 'INSOMNIA'

        digits2 = set()
        n = 0
        while len(digits2) != 10:
            n += self.n
            for d in str(n):
                digits2.add(d)

        return '{}'.format(n)

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(CountSheeps)
    p.solve()
