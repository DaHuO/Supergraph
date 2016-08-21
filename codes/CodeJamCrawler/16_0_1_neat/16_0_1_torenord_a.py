from sys import stdin

def solve(N):
    if N == 0:
        return "INSOMNIA"

    seen = set()
    i = 1

    while True:
        seen.update(set(str(i*N)))
        if len(seen) == 10:
            return i*N
        i += 1

T = int(next(stdin))

for i, N in zip(range(1, T+1), map(int, stdin)):
    print("Case #%s: %s" % (i, solve(N)))
