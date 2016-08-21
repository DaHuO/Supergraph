#!/usr/bin/env pypy3

import sys

def solve():
    N, K = map(int, input().split())
    probs = list(map(float, input().split()))
    assert(len(probs) == N)
    def recsol(cur, used, prb, prf =0):
        if cur == N-1:
            if used != K:
                return 0.0
            else:
                return prb[K//2]
        best = recsol(N-1, used, prb, prf+1)
        for j in range(cur+1, N):
            nprb = [0.0 for i in range(K+1)]
            nprb[0] = (1-probs[j])*prb[0]
            nprb[K] = probs[j]*prb[K-1]
            for k in range(1, K):
                nprb[k] = probs[j]*prb[k-1]+(1-probs[j])*prb[k]
            ans = recsol(j, used+1, nprb, prf+1)
            if ans > best:
                best = ans
        return best
    return recsol(-1, 0, [float(i == 0) for i in range(K+1)])

T = int(input())
for l in range(1, T+1):
    print("Case #%d:" % l, end=" ")
    print(solve())
