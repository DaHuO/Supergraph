from itertools import *

T = int(input())

for test in range(1, T+1):
    N, K = map(int, input().split())

    p = [float(i) for i in input().split()]

    best = 0
    for comb in combinations(p, K):
        result = 0

        for c2 in combinations(range(K), K//2):
            P = 1
            
            for i, j in enumerate(comb):
                if i in c2:
                    P *= j
                else:
                    P *= 1-j
            result += P
        
        if result > best:
            best = result

    print('Case #{}: {:.8f}'.format(test, best))

