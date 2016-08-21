# -*- coding: utf-8 -*-


def solve(k,c,s):
    # if k == s
    return " ".join([str(i) for i in range(1,k+1)])


t = int(input())
for i in range(t):
    k,c,s = [int(p) for p in input().split()]
    print("Case #" + str(i+1) + ": " + solve(k,c,s))
