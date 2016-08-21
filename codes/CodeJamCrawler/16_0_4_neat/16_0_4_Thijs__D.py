from __future__ import print_function

import collections
import math
import numpy as np
import sys

def solve(k,c,s):
    if k > c*s:
        return ["IMPOSSIBLE"]
    ret = []
    check_orig = 0L
    while check_orig < k:
        lookat = 0L
        for i in range(c):
            lookat *= k
            lookat += check_orig
            check_orig += 1
            if check_orig >= k:
                break
        ret.append(lookat + 1)
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
        #a = line.rstrip()
        ### Read one integer:
        #a = int(line)
        ### Read fixed number of integers:
        k,c,s = (int(val) for val in line.split())
        ### Read list of integers:
        #a = [int(val) for val in line.split()]

        ret = solve(k,c,s)

        # Write output
        ### Without formatting:
        #print("Case #", no, ": ", ret, sep='')
        ### Print elements of sequence separated by spaces:
        if not type(ret) is list:
            print("Warning: ret is not a list", file=sys.stderr)
        print("Case #", no, ": ", " ".join(map(str, ret)), sep='')
