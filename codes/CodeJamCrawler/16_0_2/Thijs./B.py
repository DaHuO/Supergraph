from __future__ import print_function

import collections
import math
import numpy as np
import sys

def solve(a):
    ret = 0
    prev = '+'
    for i in range(len(a) - 1, -1, -1):
        if a[i] != prev:
            ret += 1
            prev = a[i]
    return ret

if __name__ == "__main__":
    line = sys.stdin.readline() # (Note: keeps final newline)
    #print('<', line, '>', sep='')
    T = int(line)
    for no in range(1, T+1):
        print(no, "/", T, file=sys.stderr)

        # Read input for this case
        #for line in sys.stdin:
        line = sys.stdin.readline()
        ### Pass string, stripping whitespace (i.e. newline) from the end:
        a = line.rstrip()
        ### Read one integer:
        #a = int(line)
        ### Read fixed number of integers:
        #a, b = (int(val) for val in line.split())
        ### Read list of integers:
        #a = [int(val) for val in line.split()]

        ret = solve(a)

        # Write output
        print("Case #", no, ": ", ret, sep='')
