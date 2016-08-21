#!/usr/bin/env python3

def flip(s, i):
    def other(c):
        if c == '-':
            return '+'
        else:
            return '-'
    for j in range(i):
        s[j] = other(s[j])
    j = 0
    k = i-1
    while j < k:
        s[j], s[k] = s[k], s[j]
        j += 1
        k -= 1

T = int(input())
for t in range(T):
    print('Case #{}: '.format(t+1), end='')
    s = list(input())
    while len(s) and s[-1] == '+':
        s.pop()
    n = 0
    while s:
        i = 0
        while i < len(s) and s[i] == '+':
            i += 1
        if i != 0:
            flip(s, i)
            n += 1
        flip(s, len(s))
        n += 1
        while len(s) and s[-1] == '+':
            s.pop()
    print(n)
