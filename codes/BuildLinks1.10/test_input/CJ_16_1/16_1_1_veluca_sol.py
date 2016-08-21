#!/usr/bin/env pypy3

import sys

def solve(orig):
    s = orig[0]
    for c in orig[1:]:
        if c < s[0]:
            s = s + c
        else:
            s = c + s
    return s

T = int(input())
cnt = 1
for l in sys.stdin:
    print("Case #%d:" % cnt, end=" ")
    cnt += 1
    print(solve(l.strip()))
