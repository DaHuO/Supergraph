def sheep(n):
    a = set()
    if n == 0:
        return 'INSOMNIA'
    for x in xrange(1,10000):
        for c in str(n * x):
            a.add(c)
        if len(a) == 10:
            return n * x
    return 'INSOMNIA'


t = input()
for i in xrange(1, t+1):
    s = int(raw_input())
    print "Case #%d: %s" %  (i, sheep(s))
