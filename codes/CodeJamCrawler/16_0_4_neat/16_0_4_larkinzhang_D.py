#!/usr/bin/python

import sys

T = int(raw_input())

for test in range(T):
    line = raw_input().strip().split()
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])

    sys.stdout.write("Case #%d:" % (test + 1))

    for i in range(K):
        cur = 1
        for k in range(C):
            cur = cur + (i * (K ** k))

        sys.stdout.write(" %d" % cur)

    sys.stdout.write("\n")
