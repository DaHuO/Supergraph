def solve(T, N):
    seen = set()
    x = N
    for _ in xrange(10000000):
        for c in str(x):
            seen.add(c)
        if len(seen) == 10:
            print "Case #{}: {}".format(T, x)
            return
        x += N
    print "Case #{}: {}".format(T, "INSOMNIA")


if __name__ == '__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        line = raw_input().split()
        solve(i, int(line[0]))
