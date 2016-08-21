#!/usr/bin/python

def solve(K, C, S):
    return [str(K ** (C - 1) * k + 1) for k in range(K)]

T = int(input())
for t in range(T):
    K, C, S = map(int, input().split())
    ans = solve(K, C, S)
    print('Case #{}: {}'.format(t + 1,  ' '.join(ans)))

