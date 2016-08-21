#!/bin/python3

def solve():
    T = int(input())
    for t in range(1, T+1):
        K,C,S = map(int, input().split())
        ans = solveCase(K,C,S)
        if ans:
            print("Case #{0}: {1}".format(t, ' '.join(map(str, ans))))
        else:
            print("Case #{0}: IMPOSSIBLE".format(t))

def solveCase(K, C, S):
    N = K**C
    if S * C < K:
        return []
    ans = []
    for i in range(0, K, C):
        t = N
        pos = 0
        for a in range(C):
            #print(t,K,t//K)
            t = t // K

            pos += t * min(i+a, K-1)
        ans.append(pos+1)
    return ans

solve()
