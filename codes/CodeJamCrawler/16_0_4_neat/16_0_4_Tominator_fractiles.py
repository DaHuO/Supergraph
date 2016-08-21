#!/usr/bin/env python3
# This handles the small inputs only (K = S).
# Student #x chooses the x-th tile each time.

import sys

def find_tiles(K, C):
    if K == 1:
        return [1]

    tiles = []
    # form the numbers 000, 111, 222, etc., in base K, each one of length C
    for i in range(K):
        s = [i] * C
        tiles.append(int_in_base(s, K) + 1)
    return tiles

def int_in_base(digits, base):
    place_value = 1
    number = 0

    for digit in reversed(digits):
        number += place_value * digit
        place_value *= base

    return number


num_tests = int(sys.stdin.readline().strip())

for i in range(num_tests):
    K, C, S = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    if K == S:
        result = find_tiles(K, C)
    else:
        result = "UNKNOWN"

    print("Case #%d: %s" % (i+1, " ".join(str(x) for x in result)))

