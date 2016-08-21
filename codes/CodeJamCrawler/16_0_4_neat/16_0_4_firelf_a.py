t = int(raw_input())
for index in xrange(1, t+1):
    k,c,s = map(int, raw_input().split(' '))
    res = [i for i in xrange(1, k**c+1, k**(c-1))]
    print 'Case #{}: {}'.format(index, ' '.join(map(str,res)))
