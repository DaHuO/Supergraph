def solve(N):
    l = 0
    d = set()
    x = N
    while l < 40:
        subs = set(str(x))
        if subs.issubset(d):
            l += 1
        else:
            l = 0
            d.update(subs)
        if len(d) == 10:
            return x
        x += N
    return 'INSOMNIA'

tests_count = int(raw_input())
for i in xrange(1, tests_count + 1):
    N = int(raw_input())
    print 'Case #{0}: {1}'.format(i, solve(N))
