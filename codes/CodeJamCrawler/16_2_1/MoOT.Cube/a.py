#!/usr/bin/env python

import sys
from collections import defaultdict
import operator

NUMBERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def toto(n):
    l = defaultdict(int)
    for c in n:
        l[c] += 1
    return l

MAPPED_NUMBERS = [dict(toto(n)) for n in NUMBERS]

LETTERS = defaultdict(list)
for k,d in enumerate(MAPPED_NUMBERS):
    for l,v in d.items():
        LETTERS[l].append(k)

LETTERS = sorted(LETTERS, key=lambda k: len(k))


if __name__ == "__main__":
    for (k, i) in enumerate([l.rstrip("\n") for l in sys.stdin.readlines()[1:]]):
        letters = defaultdict(int)
        for l in i:
            letters[l] += 1
        output = []
        heigths = letters['G']
        output += [8]*heigths
        for l,v in MAPPED_NUMBERS[8].items():
            letters[l] -= v * heigths
        twos = letters['W']
        output += [2]*twos
        for l,v in MAPPED_NUMBERS[2].items():
            letters[l] -= v * twos
        sixs = letters['X']
        output += [6]*sixs
        for l,v in MAPPED_NUMBERS[6].items():
            letters[l] -= v * sixs
        zeros = letters['Z']
        output += [0]*zeros
        for l,v in MAPPED_NUMBERS[0].items():
            letters[l] -= v * zeros
        fours = letters['U']
        output += [4]*fours
        for l,v in MAPPED_NUMBERS[4].items():
            letters[l] -= v * fours

        fives = letters['F']
        output += [5]*fives
        for l,v in MAPPED_NUMBERS[5].items():
            letters[l] -= v * fives
        threes = letters['H']
        output += [3]*threes
        for l,v in MAPPED_NUMBERS[3].items():
            letters[l] -= v * threes
        sevens = letters['S']
        output += [7]*sevens
        for l,v in MAPPED_NUMBERS[7].items():
            letters[l] -= v * sevens

        nines = letters['I']
        output += [9]*nines
        for l,v in MAPPED_NUMBERS[9].items():
            letters[l] -= v * nines

        ones = letters["O"]
        output += [1]*ones
        s = "".join([str(v) for v in sorted(output)])
        print("Case #" + str(k + 1) + ": " + s)
