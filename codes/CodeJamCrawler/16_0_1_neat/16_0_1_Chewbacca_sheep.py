#! /usr/bin/env python3
# Written by Krzysio Leszczyński <chris@camk.edu.pl>
# Code Jam 2016

import sys


full_set = set(range(10))
def max_0_9(n):
    s = set()
    for k in range(1,100):
        s |= set(str(k*n))
        if s==max_0_9.full_set:
            return k*n
    return "INSOMNIA"
max_0_9.full_set = set(map(str,range(10)))

test_cases = int(sys.stdin.readline())

for tcase in range(1, test_cases+1):
    N = int(sys.stdin.readline())
    print("Case #{}: {}".format(tcase,max_0_9(N)))

