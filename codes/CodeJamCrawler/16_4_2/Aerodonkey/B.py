import sys
from itertools import combinations

T = int(sys.stdin.readline())
for x in range(1, T + 1):
    tokens = sys.stdin.readline().split()
    N = int(tokens[0])
    K = int(tokens[1])
    tokens = sys.stdin.readline().split()
    P = [float(p) for p in tokens]
    y = 0.0
    I = range(N)
    for c in combinations(I, K):
        sum = 0.0
        for h in combinations(c, K // 2):
            prod = 1.0
            for i in c:
                if i in h:
                    prod *= P[i]
                else:
                    prod *= 1.0 - P[i]
            sum += prod
        y = max(y, sum)
    sys.stdout.write('Case #{}: {}\n'.format(x, y))
    sys.stdout.flush()
