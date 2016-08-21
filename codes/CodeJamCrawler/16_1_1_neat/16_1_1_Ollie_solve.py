#!/usr/bin/python3

def solve(s):
    lw = s[0]
    for c in s[1:]:
        if c >= lw[0]:
            lw = c + lw
        else:
            lw = lw + c
    return lw

t = int(input())
for i in range(1,t+1):
    s = input()
    print("Case #%d: %s" % (i, solve(s)))
