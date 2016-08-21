#!/usr/bin/env python3

import numpy as np

def solve(pancakes):
    m = 0
    for i in reversed(range(len(pancakes))):
        if not pancakes[i]:
            pancakes[:i+1] ^= True
            m += 1
    return m

T = int(input())
for t in range(1, T + 1):
    pancakes = np.array(list(input())) == "+"
    print("Case #%d: %d" % (t, solve(pancakes)))
