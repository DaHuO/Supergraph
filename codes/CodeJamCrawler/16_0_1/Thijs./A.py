from __future__ import print_function

import collections
import math
import numpy as np
import sys

def solve(a):
    if a == 0:
        return "INSOMNIA"
    seen = np.zeros(10, dtype=bool)
    cur = 0
    while True:
        cur += a
        s = str(cur)
        for c in s:
            seen[int(c)] = True
        if np.all(seen):
            break
    return cur

if __name__ == "__main__":
    line = sys.stdin.readline() # (Note: keeps final newline)
    #print('<', line, '>', sep='')
    T = int(line)
    for no in range(1, T+1):
        print(no, "/", T, file=sys.stderr)

        # Read input for this case
        #for line in sys.stdin:
        line = sys.stdin.readline()
        ### Read one integer:
        a = int(line)
        ### Read fixed number of integers:
        #a, b = (int(val) for val in line.split())
        ### Read list of integers:
        #a = [int(val) for val in line.split()]

        ret = solve(a)

        # Write output
        print("Case #", no, ": ", ret, sep='')
