#!/usr/bin/env python

"""
Problem

Long ago, the Fractal civilization created artwork consisting of linear rows of tiles. They had two types of tile that they could use: gold (G) and lead (L).

Each piece of Fractal artwork is based on two parameters: an original sequence of K tiles, and a complexity C. For a given original sequence, the artwork with complexity 1 is just that original sequence, and the artwork with complexity X+1 consists of the artwork with complexity X, transformed as follows:

replace each L tile in the complexity X artwork with another copy of the original sequence
replace each G tile in the complexity X artwork with K G tiles
For example, for an original sequence of LGL, the pieces of artwork with complexity 1 through 3 are:

C = 1: LGL (which is just the original sequence)
C = 2: LGLGGGLGL
C = 3: LGLGGGLGLGGGGGGGGGLGLGGGLGL
Here's an illustration of how the artwork with complexity 2 is generated from the artwork with complexity 1:

You have just discovered a piece of Fractal artwork, but the tiles are too dirty for you to tell what they are made of. Because you are an expert archaeologist familiar with the local Fractal culture, you know the values of K and C for the artwork, but you do not know the original sequence. Since gold is exciting, you would like to know whether there is at least one G tile in the artwork. Your budget allows you to hire S graduate students, each of whom can clean one tile of your choice (out of the KC tiles in the artwork) to see whether the tile is G or L.

Is it possible for you to choose a set of no more than S specific tiles to clean, such that no matter what the original pattern was, you will be able to know for sure whether at least one G tile is present in the artwork? If so, which tiles should you clean?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with three integers: K, C, and S.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if no set of tiles will answer your question, or a list of between 1 and S positive integers, which are the positions of the tiles that will answer your question. The tile positions are numbered from 1 for the leftmost tile to KC for the rightmost tile. Your chosen positions may be in any order, but they must all be different.

If there are multiple valid sets of tiles, you may output any of them. Remember that once you submit a Small and it is accepted, you will not be able to download and submit another Small input. See the FAQ for a more thorough explanation. This reminder won't appear in problems in later rounds.

Limits

1 <= T <= 100.
1 <= K <= 100.
1 <= C <= 100.
KC <= 10e18.

Small dataset

S = K.
Large dataset

1 <= S <= K.
"""

def get_tiles_formatted(k, c, s):
    assert s >= k, "Not enough peeks for this lazy method"
    tiles = list(range(1, k + 1))
    return " ".join(str(t) for t in tiles)

if __name__ == "__main__":
    t = int(raw_input())
    for case_num in range(1, t + 1):
        k, c, s = [int(s) for s in raw_input().split(" ")]
        print "Case #{}: {}".format(case_num, get_tiles_formatted(k, c, s))
