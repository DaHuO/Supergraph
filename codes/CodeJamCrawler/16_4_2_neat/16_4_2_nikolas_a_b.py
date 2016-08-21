import numpy as np
from itertools import combinations

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    P = map(float, input().split())
    
    best = 0.0
    for comb in combinations(P, K):
        dist = np.array(1.0)
        for p in comb:
            dist = np.convolve(dist, [1-p, p])
        best = max(best, dist[K/2])

    print("Case #%d: %.8f" % (t, best))
