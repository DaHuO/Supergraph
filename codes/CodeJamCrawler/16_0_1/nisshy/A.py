def solve():
    N = input()
    if N == 0: return 'INSOMNIA'

    S = set()
    x = 0
    while True:
        x += N
        S |= set(str(x))
        if len(S) == 10: return x

T = input()
for t in xrange(1, T + 1):
    print 'Case #%d: %s' % (t, solve())
