#!/usr/bin/env python3
"""
Problem D. Fractiles
CodeJam 2016: Qualification Round
https://code.google.com/codejam/contest/6254486/dashboard#s=p3

How to run:
$ ./fractiles.py < sample.in > sample.out

Validate:
$ diff -s sample.out sample.out.key
Files sample.out and sample.out.key are identical
"""
from itertools import product


__author__ = "Tatiana Al-Chueyr"
__email__ = "tatiana.alchueyr@gmail.com"
__date__ = "2016-04-09"
__version__ = "1.1.0"


def minimum_clean_tiles(tiles, complexity):
    """
    Return the minimal number of tiles that must be cleaned, given:
    - tiles (K): number of tiles which make the original pattern
    - complexity (C): fractal complexity (expansion)
    """
    # When there is no fractal, we have a simple combination of 2 values (GL) 
    # of size #tiles (K) - which ends up something similar to:
    #   LLL
    #   LLG
    #   LGL
    #   GLL
    #   GLG
    #   GGL
    #   GGG
    # in this case, the only way to guarantee any occurence of G will be mapped
    # will be validating the K columns.
    #
    # However, when there is a fractal factor, the result resambles:
    #   LLLLLLLLL
    #   LLGLLGGGG
    #   LGLGGGLGL
    #   LGGGGGGGG
    #   GGGGLLGLL
    #   GGGGLGGGG
    #   GGGGGGGGL
    #   GGGGGGGGG
    # (example for #tiles (K) == 3 and complexity (C) == 2)
    # After plotting a few of these representations (including large Ks and Cs),
    # it is possible to see that the most significant columns are the first K,
    # except for the first (because the 2nd colum already contains all the 
    # occurences of Gs in the 1st). The behavior for K=3 and C=2 can be seen as:
    #   (G in (K-0)th column): unique occurences: 1 (2**8)/4
    #   (G in (K-1)th column): unique occurences: 2 (2**8)/4
    #   (G in (K-2)th column): unique occurences: 4 (2**8)/2
    # This can be generalized to conclude that - if a factorila C>=2 is applied,
    # only (K - 1) need to be checked.
    if complexity == 1:
        response = tiles
    else:
        response = tiles - 1
    return response


def tiles_to_be_cleaned(tiles, complexity):
    """
    Return a list containing the tiles that should be cleaned, given:
    - tiles (K): number of tiles which make the original pattern
    - complexity (C): fractal complexity (expansion)
    """
    i = minimum_clean_tiles(tiles, complexity)
    to_be_cleaned = []
    n = tiles
    while i:
        to_be_cleaned.append(n)
        n -= 1
        i -=1
    return sorted(to_be_cleaned)


def solve(tiles, complexity, students):
    """
    Is it possible for you to choose a set of no more than S specific tiles to
    clean, such that no matter what the original pattern was, you will be able
    to know for sure whether at least one G tile is present in the artwork?
    If so, which tiles should you clean?

    Input:
    - tiles (K): number of tiles which make the original pattern
    - complexity (C): fractal complexity (expansion)
    - students (S): number of tiles to be cleaned

    Output:
    - "IMPOSSIBLE" if it is not feasible
    - i j k : sequence of integers, related to the tiles which should be cleaned
    """
    if students < minimum_clean_tiles(tiles, complexity):
        response = "IMPOSSIBLE"
    else:
        if students >= tiles:
            complexity = 1 # force to check all tiles to see if we pass small set
        values = tiles_to_be_cleaned(tiles, complexity)
        response = " ".join([str(value) for value in values])
    return response
    

if __name__ == "__main__":
    TOTAL = int(input())
    for i in range(1, TOTAL + 1):
        k, c, s = [int(s) for s in input().split(" ")]
        response = solve(k, c, s)
        print("Case #{}: {}".format(i, response))
