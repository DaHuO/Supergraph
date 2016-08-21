T = int(raw_input())

ds = set('0123456789')

for i in range(1, T + 1):
    N = int(raw_input())

    if N == 0:
        print 'Case #%d: INSOMNIA' % i
        continue
    
    K = N
    S = set(str(K))
    while not ds.issubset(S):
        K += N
        S |= set(str(K))
    
    print 'Case #' + str(i) + ':', K
