#!/usr/bin/env python

TEST="""5
-
-+
+-
+++
--+-"""
#raw_input = iter(TEST.splitlines()).next

def solve(S):
    c = ""
    flips = 0
    for p in S:
        if p != c:
            flips += 1
        c = p
    if c == "+":
        return flips-1
    return flips


T = int(raw_input())
for case in range(1,T+1):
    STACK = raw_input().strip()
    print("Case #%s: %s" % (case, solve(STACK)))
