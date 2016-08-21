import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    if N == 0:
        print("Case #{}: INSOMNIA".format(t+1))
    else:
        seen = [False for x in range(10)]
        n = 0
        while not all(seen):
            n += N
            for c in str(n):
                seen[int(c)] = True
        print("Case #{}: {}".format(t+1, n))


