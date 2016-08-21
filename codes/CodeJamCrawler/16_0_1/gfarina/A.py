def solve():
    N = input()
    seen = [False] * 10
    for i in xrange(1, 2000):
        for digit in str(i * N):
            seen[int(digit)] = True
        if all(seen):
            return N * i
    return 'INSOMNIA'

T = input()
for t in xrange(T):
    print 'Case #%d:' % (t + 1,), solve()
