#!/usr/bin/env python
num = int(raw_input())

def solve(s):
    state = '+'
    x = 0
    s = list(s)
    s = s[::-1]
    for char in s:
        if char != state:
            x += 1
            state = char
    return x

for i in range(1, num+1):
    n = solve(raw_input())
    print "Case #{}:".format(i), n


