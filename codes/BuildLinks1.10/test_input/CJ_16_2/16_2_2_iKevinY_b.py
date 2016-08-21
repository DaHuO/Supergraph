import os
import sys
import re
import math
from itertools import product, permutations, combinations, combinations_with_replacement

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

def memoize(f):
    """Simple dictionary-based memoization decorator"""
    cache = {}
    def _mem_fn(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    _mem_fn.cache = cache
    return _mem_fn

# -----------------------

num_cases = int(raw_input())
num_lines = 1

DIGITS = "1234567890"

for case in range(1, num_cases + 1):
    # Declare variables for case
    out = None

    # Possible first "setup line" which might determine num_lines
    # a, b = raw_input().strip().split()

    for _ in range(num_lines):
        line = raw_input()

    # Perform computation on case information
    C, J = [x for x in line.split()]

    C_poss = [C]
    J_poss = [J]

    while '?' in C_poss[0]:
        tmp = []
        for p in C_poss:
            tmp2 = []
            for d in DIGITS:
                tmp2.append(p.replace('?', d, 1))

            tmp.extend(tmp2)

        C_poss = tmp

    while '?' in J_poss[0]:
        tmp = []
        for p in J_poss:
            tmp2 = []
            for d in DIGITS:
                tmp.append(p.replace('?', d, 1))

            tmp.extend(tmp2)

        J_poss = tmp

    min_diff = min(abs(int(x) - int(y)) for x, y in product(C_poss, J_poss))

    C_min = '10000'
    J_min = '10000'

    for x, y in product(C_poss, J_poss):
        if abs(int(x) - int(y)) == min_diff:
            if int(x) <= int(C_min):
                if int(y) <= int(J_min):
                    C_min, J_min = x, y

    print "Case #{}: {} {}".format(case, C_min, J_min)

