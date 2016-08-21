#!/usr/bin/python

import string
import sys

def solve(i):
    K, C, S = [int(x) for x in sys.stdin.readline().split()]
    output = ' '.join([str(x) for x in range(1, S+1)])
    print "Case #{}: {}".format(i, output)

T = int(sys.stdin.readline())
for i in range(T):
    solve(i+1)

