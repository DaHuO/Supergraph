def get_digs(n):
    n_str = str(n)
    return set([int(c) for c in n_str])     

T = int(raw_input())

for t in range(1, T+1):
    n = int(raw_input())
    if n == 0:
        print 'Case #%d: INSOMNIA' % t
        continue
    ds = get_digs(n)
    for i in xrange(2, 10000000000):
        if len(ds) >= 10:
            print 'Case #%d: %d' % (t, n *(i-1))
            break
        ds = ds.union(get_digs(n*i))
        
