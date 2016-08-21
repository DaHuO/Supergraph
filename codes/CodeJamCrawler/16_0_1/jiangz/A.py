#! /usr/bin/env python3

import string

def solve(n):
    s = set()
    for x in range(1, 1000000):
        s |= set(str(n*x))
        if all(map(lambda x: x in s, string.digits)):
            return n*x
    return 'INSOMNIA'


T = int(input())

for i in range(T):
    N = int(input())
    print('Case #{}: {}'.format(i+1, solve(N)))
