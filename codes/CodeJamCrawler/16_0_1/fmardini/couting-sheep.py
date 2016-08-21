import os, sys, copy

def solve(n):
    seen = set()
    x = n
    for i in range(1000):
        seen.update(c for c in str(n))
        if len(seen) == 10:
            return str(n)
        n += x
    return "INSOMNIA"

T = int(sys.stdin.readline().strip())
for k in range(T):
    N = int(sys.stdin.readline().strip())
    print("Case #{}: {}".format(k + 1, solve(N)))
