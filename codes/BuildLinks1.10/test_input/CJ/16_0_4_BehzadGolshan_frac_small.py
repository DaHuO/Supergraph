n = int(raw_input())
for itt in xrange(n):
    instance = raw_input().strip()
    (k, c, s) = map(int, instance.split(' '))
    # solving the problem
    print 'Case #' + str(itt + 1) + ':',
    interval = k ** (c - 1);
    for i in xrange(k): print 1 + interval * i,
    print
