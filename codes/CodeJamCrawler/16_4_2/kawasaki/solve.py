T = int(raw_input())
for tc in xrange(1, T + 1):
    N, K = map(int, raw_input().split())
    P = map(float, raw_input().split())

    def bitcount(n):
        c = 0
        while 0 < n:
            c += 1
            n = (n - 1) & n
        return c

    def solve():
        maxp = 0.0
        for kflags in xrange(1 << N):
            if bitcount(kflags) != K:
                continue

            ps = [P[i] for i in xrange(N) if (1 << i) & kflags]
            assert len(ps) == K
            p = 0
            for pflags in xrange(1 << K):
                ns = [1 if (1 << i) & pflags else 0 for i in xrange(K)]
                if sum(ns) == K >> 1:
                    ptmp = [ps[i] if ns[i] else 1 - ps[i] for i in xrange(K)]
                    p += reduce(lambda a, b: a * b, ptmp, 1.0)
            maxp = max(maxp, p)
        return maxp

    print 'Case #{}: {}'.format(tc, solve())
