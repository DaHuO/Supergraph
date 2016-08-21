def sol(n):
    s = set()
    for i in xrange(1, 1000):
        s.update(str(i * n))
        if len(s) == 10:
            return i * n
    return 'INSOMNIA'


rl = lambda: map(int, raw_input().split())

t = input()
for i in xrange(t):
    a = input()
    print "Case #%d:" % (i + 1), sol(a)
