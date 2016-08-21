import os, sys

def solve(K, C, S):
    return ' '.join(map(str, range(1, S + 1)))

T = int(sys.stdin.readline().strip())
for k in range(T):
    K, C, S = map(int, sys.stdin.readline().strip().split())
    print("Case #{}: {}".format(k + 1, solve(K, C, S)))
