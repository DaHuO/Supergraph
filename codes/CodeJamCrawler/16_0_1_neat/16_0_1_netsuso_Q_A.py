#!/usr/bin/python3

import sys

ncases = int(sys.stdin.readline().strip())

for t in range(1, ncases+1):
    n = int(sys.stdin.readline().strip())

    current = n
    digits = {}
    i = 0
    found = False
    while i < 1000:
        currentstr = str(current)
        for c in currentstr:
            digits[c] = True
        if len(digits.keys()) >= 10:
            found = True
            break
        current += n
        i += 1

    if found:
        print("Case #{0}: {1}".format(t, current))
    else:
        print("Case #{0}: INSOMNIA".format(t))

