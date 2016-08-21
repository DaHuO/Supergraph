import sys

rl = lambda: sys.stdin.readline().strip()


T = int(rl())
for tcase in range(1, T + 1):
    N = int(rl())
    if N == 0:
        print 'Case #%d: INSOMNIA' % tcase
        continue
    seen = set()
    for i in range(1, 10001):
        n = N * i
        a = n
        while True:
            a, b = divmod(a, 10)
            seen.add(b)
            if not a:
                break
        if len(seen) >= 10:
            break
    print 'Case #%d: %d' % (tcase, n)
