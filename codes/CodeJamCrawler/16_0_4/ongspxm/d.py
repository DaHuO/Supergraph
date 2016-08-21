N = input()
for n in range(N):
    k, c, s = [int(c) for c in raw_input().split(' ')]
    a = ' '.join([str(i+1) for i in range(k)])

    print 'Case #%d: %s'%(n+1, a)

