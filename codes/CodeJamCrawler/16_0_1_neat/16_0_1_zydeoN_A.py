#!/usr/bin/env python3

from numpy import float64   # so that float64(1)/0 == inf (avoid errors)
inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def digits(N):
    ans = set()
    while N != 0:
        ans.add(N % 10)
        N //= 10
    return ans

def solve(N):
    S = set()
    for i in range(1, 1000001):
        S |= digits(N*i)
        if len(S) == 10:
            return N*i
    return None

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        ans = solve(N)
        if ans == None:
            print("Case #%d: INSOMNIA" % (tc))
        else:
            print("Case #%d: %d" % (tc, ans))
