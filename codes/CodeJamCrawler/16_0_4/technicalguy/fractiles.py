#!/usr/bin/env python
import fileinput

def fractiles(line):
    [k, c, s] = [int(x) for x in line.split(" ")]
    if s * c < k:
        return "IMPOSSIBLE"
    i = 0
    acc = 0
    checks = []
    for p in range(0, k):
        acc += p * (k ** (c - 1 - i))
        i += 1
        if i == c:
            i = 0
            checks.append(acc)
            acc = 0
    if i > 0:
        checks.append(acc)
    return " ".join(str(x + 1) for x in checks)

i = 0
for line in fileinput.input():
    if i == 0:
        i += 1
        continue
    print("Case #" + str(i) + ": " + fractiles(line))
    i += 1
