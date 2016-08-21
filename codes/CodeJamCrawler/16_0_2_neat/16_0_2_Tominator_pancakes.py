#!/usr/bin/env python3

import sys

def number_of_flips(s):
    s += "+"
    count = 0

    for ch1, ch2 in zip(s, s[1:]):
        if ch1 != ch2:
            count += 1
    return count

num_tests = int(sys.stdin.readline().strip())
for i in range(num_tests):
    s = sys.stdin.readline().strip()
    print("Case #%d: %d" % (i+1, number_of_flips(s)))

