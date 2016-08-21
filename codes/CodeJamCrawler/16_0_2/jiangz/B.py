#!/usr/bin/env python3

T = int(input())

def group(s):
    res = [s[0]]
    for state in s:
        if state != res[-1]:
            res.append(state)
    return res

def count(s):
    res = 0
    for state in s:
        if state == '-':
            res += 2
    if s[0] == '-':
        res -= 1
    return res

for i in range(T):
    s = input()
    santized = group(s)
    print('Case #{}: {}'.format(i+1, count(santized)))
