#!/usr/bin/env python

TEST="""5
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3"""
#raw_input = iter(TEST.splitlines()).next

def solve(K,C,S):
    if K == S:
        return " ".join(map(str, range(1,S+1)))
    return "IMPOSSIBLE"

T = int(raw_input())
for case in range(1,T+1):
    K,C,S = map(int, raw_input().strip().split())
    print("Case #%s: %s" % (case, solve(K,C,S)))
