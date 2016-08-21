#!/usr/bin/env python3
import numpy as np

def flip(pans, n):
    pans[0:n] = np.invert(pans[0:n])

T = int(input())
for i in range(1, T + 1):
    pans = np.array(list(input())) == '+'
    flips = 0
    if len(pans) > 1:
        for pan in range(1, len(pans)):
            if np.all(pans): break
            if pans[pan] != pans[pan-1]:
                flip(pans, pan)
                flips += 1
            if pan == len(pans) - 1 and not pans[pan]:
                flip(pans, pan)
                flips += 1
    else:
        flips = 0 if np.all(pans) else 1

    print("Case #{}: {}".format(i, flips))
