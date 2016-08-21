#!/usr/bin/python3
# Valid only for the trivial small case

import sys

ncases = int(sys.stdin.readline().strip())

for t in range(1, ncases+1):
    values = sys.stdin.readline().strip().split()
    k = int(values[0])
    c = int(values[1])
    s = int(values[2])

    print("Case #{0}:".format(t), end="")
    for i in range(1, k+1):
        print(" {0}".format(i), end="")
    print()

