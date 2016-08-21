#!/usr/bin/python3

import sys

T = int(sys.stdin.readline().strip())

for ncase in range(T):
    K, C, S = sys.stdin.readline().strip().split(' ')
    K = int(K)
    C = int(C)
    S = int(S)
    print("Case #%d: %s" % (ncase + 1,
        ' '.join(str(x) for x in range(1,S+1))))
