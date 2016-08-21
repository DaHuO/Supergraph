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

nums = {
    "ZERO": 0,  # Z
    "ONE": 1,
    "TWO": 2,  # W
    "THREE": 3,
    "FOUR": 4,  # U
    "FIVE": 5,
    "SIX": 6,  # X
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
}



for case in range(1, num_cases + 1):
    # Declare variables for case
    out = None
    number = []

    # Possible first "setup line" which might determine num_lines
    # a, b = raw_input().strip().split()

    for _ in range(num_lines):
        line = raw_input().strip()

    letters = sorted(line)

    for x in range(len(letters) // 5, len(letters) // 3 + 1):
        for p in product(nums.keys(), repeat=x):
            if sorted(''.join(p)) == letters:
                for z in p:
                    number.append(nums[z])
                break
        else:
            out = ''

    number = sorted(number)


    print "Case #{}: {}".format(case, ''.join(str(s) for s in number))
