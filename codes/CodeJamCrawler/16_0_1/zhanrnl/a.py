def f(k):
    seen_ds = set()
    for j in xrange(1,100):
        nk = j * k
        seen_ds = seen_ds | set(str(nk))
        if len(seen_ds) >= 10:
            return nk
    return 'INSOMNIA'
n = int(raw_input())
for i in xrange(n):
    k = int(raw_input())
    print 'Case #{}: {}'.format(i+1, f(k))
