#!/usr/bin/env python3

def sheep(n):                                                                    
    if n == 0:
        return "INSOMNIA"

    k = n
    digits = set(str(n))
    while len(digits) != 10:
        k += n
        digits = digits.union(str(k))
    return k

with open('A-large.in', 'r') as infile:
    lines = infile.readlines()[1:]
    for i, n in enumerate(lines):
        print("Case #{}:".format(i + 1), sheep(int(n)))
