#! /usr/bin/env python
from __future__ import print_function, division
try:
    range = xrange
except NameError:
    pass

# import collections
# import functools
import itertools as it
# import numpy as np # See http://www.numpy.org
# import sympy as sp # See http://sympy.org/en/index.html
# import gmpy2 # See https://code.google.com/p/gmpy/
# import networkx as nx # See http://networkx.github.io/

import os
import sys
# MY MODULES - available at https://github.com/lackofcheese/CodeJamLib/
sys.path.append(os.path.join(
    os.environ['GOOGLE_DRIVE'], 'Coding', 'GCJ', 'CodeJamLib'))
import codejam_io

def toks_line(f_in, fun=int):
    return [fun(k) for k in f_in.readline().split()]

def process_first(f_in):
    num_cases = int(f_in.readline())
    other_data = None
    return num_cases, other_data

def process_case(f_in, f_out, case_no, other_data=None):
    N, R, P, S = toks_line(f_in)
    ans = solve(N, R, P, S)
    if ans is None:
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(case_no, ans), file=f_out)

def solve(N, R, P, S):
    lineups = []
    players = "R" * R + "P" * P + "S" * S
    for perm in it.permutations(players):
        lineup = ''.join(perm)
        for i in range(N):
            lineup = round(lineup)
            if lineup is None:
                break
        if lineup is not None:
            lineups.append(''.join(perm))
    if not lineups:
        return None
    lineups.sort()
    return lineups[0]

def round(lineup):
    new_lineup = ""
    for i in range(len(lineup)//2):
        winner = fight(lineup[i*2], lineup[i*2+1])
        if winner is None:
            return None
        new_lineup += winner
    return new_lineup

WINNERS = dict([
        (frozenset(['R', 'P']), 'P'),
        (frozenset(['R', 'S']), 'R'),
        (frozenset(['S', 'P']), 'S')
        ])

def fight(a, b):
    if a == b:
        return None
    else:
        return WINNERS[frozenset([a, b])]

if __name__ == '__main__':
    codejam_io.process_input(process_case, process_first, __file__)
