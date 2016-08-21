def solve(N):
    seen = set()
    for i in range(1, 100):
        n = i * N
        for c in str(n):
            seen.add(c)
        if len(seen) == 10:
            return n
    return "INSOMNIA"

T = int(input())
for t in range(T):
    N = int(input())
    print('Case #{}: {}'.format(t + 1, solve(N)))
