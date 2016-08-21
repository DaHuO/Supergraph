#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal
import math

from codejam.common import CodeJamIO, Problem, ProblemInstance


#===============================================================================
# Store credit problem
#===============================================================================
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def mypow(x, n):
    s = 1L
    for _ in range(n):
        s *= x
    return s


class Fractiles(ProblemInstance):

    def __init__(self):
        self.k, self.c, self.s = CodeJamIO.read_int_multi()
        #self.k_pow_c = [math.pow(self.k, cs) for cs in range(self.c)]
        self.k_pow_c = [mypow(self.k, cs) for cs in range(self.c)]

    def solve1(self):
        min_s = math.ceil(self.k / float(self.c))
        if self.s < min_s:
            return 'IMPOSSIBLE'

        solution_1 = range(1, self.k + 1)
        solution_chunks = list(chunks(solution_1, self.c))

        last_chunk = solution_chunks[-1]
        if len(last_chunk) < self.c:
            if self.k > self.c:
                solution_chunks[-1] = [1] * (self.c - len(last_chunk)) + last_chunk

        solution = [str(self.compute_index(chunk)) for chunk in solution_chunks]

        return ' '.join(solution)

    def compute_index(self, chunk):
        # reverse order index
        chunk_contribution_factors = list(enumerate(reversed(chunk)))
        #chunk_contribution = [e * self.k_pow_c[idx] for idx, e in chunk_contribution_factors]
        chunk_contribution = [(e - 1) * self.k_pow_c[idx] for idx, e in chunk_contribution_factors]
        return int(sum(chunk_contribution) + 1)

    def solve(self):
        min_s = math.ceil(self.k / float(self.c))
        if self.s < min_s:
            return 'IMPOSSIBLE'

        level1 = range(self.k)
        solution_chunks = list(chunks(level1, self.c))
        solution = [self.compute_index2(chunk) for chunk in solution_chunks]

        return ' '.join([str(x) for x in solution])

    def compute_index2(self, chunk):
        # reverse order index
        chunk_contribution_factors = list(enumerate(reversed(chunk)))
        #chunk_contribution = [e * self.k_pow_c[idx] for idx, e in chunk_contribution_factors]
        chunk_contribution = [self.k_pow_c[idx] * e for idx, e in chunk_contribution_factors]
        index = sum(chunk_contribution) + 1L
        return index

#------------------------------------------------------------------------------

if __name__ == '__main__':
    p = Problem(Fractiles)
    p.solve()
