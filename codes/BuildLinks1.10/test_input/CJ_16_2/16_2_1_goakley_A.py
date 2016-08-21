#!/usr/bin/env python3

from collections import defaultdict

LETTERS = list(zip(range(10), ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]))

def solve(vals, letters):
    if len(letters) == 0:
        if all(v == 0 for v in vals.values()):
            return ""
        return None
    recursed = solve(vals, letters[1:])
    if recursed is not None:
        return recursed
    l = letters[0][1]
    for c in l:
        vals[c] -= 1
    current = str(letters[0][0])
    for c in l:
        if vals[c] < 0:
            current = None
    if current is not None:
        recursed = solve(vals, letters)
        if recursed is not None:
            current = current + recursed
        else:
            current = None
    for c in l:
        vals[c] += 1
    return current

def readinput(val):
    result = defaultdict(int)
    for c in val:
        result[c] += 1
    return result

n = int(input())
for i in range(n):
    print("Case #{}: {}".format(i + 1, solve(readinput(input()), LETTERS)))
