T = int(input())

for t in range(1, T+1):
    N = int(input())

    if N == 0:
        print("Case #%d: INSOMNIA" % t)
        continue

    inc = N

    visited = set([int(n) for n in str(N)])

    while len(visited) < 10:
        N += inc
        visited = visited.union([int(n) for n in str(N)])

    print("Case #%d: %d" % (t, N))