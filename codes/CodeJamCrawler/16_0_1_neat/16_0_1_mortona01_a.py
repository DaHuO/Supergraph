#!/usr/bin/env python

import sys

stdin = sys.stdin
T = int(stdin.readline())

for i in range(1, T+1):
    N = int(stdin.readline().rstrip())
    # print "N: {}".format(N)

    if N == 0:
        print "Case #{}: {}".format(i, "INSOMNIA")
        continue

    digits_seen = {}
    breakout = False
    j = 0
    while not breakout:
        j += 1
        current_num = N * j
        # print "digits: {}".format(digits_seen)
        for d in str(current_num):
            if d not in digits_seen:
                digits_seen[d] = True
                if len(digits_seen) == 10:
                    breakout = True
                    break

    print "Case #{}: {}".format(i, current_num)
