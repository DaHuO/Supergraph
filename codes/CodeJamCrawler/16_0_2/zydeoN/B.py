#!/usr/bin/env python3

from numpy import float64   # so that float64(1)/0 == inf (avoid errors)
inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def solve(S):
    last = S[0]
    ans  = 0
    for p in S:
        if p != last:
            ans+=1
        last = p
    if last == '-':
        ans += 1
    return ans

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        S = input()
        print("Case #%d: %d" % (tc, solve(S)))