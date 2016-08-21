#!/usr/bin/env python

tcase = input()

for i in xrange(1,tcase+1):
    K, C, S = map(int, raw_input().split(' '))
    print 'Case #%d:' % i,
    if C == 1:
        if K == S:
            print reduce(lambda a,b:str(a)+' '+str(b), range(1, S+1))
        else:
            print 'IMPOSSIBLE'
        continue

    if K == 1:
        print 1
        continue

    if S < K-1:
        print 'IMPOSSIBLE'
        continue

    for i in xrange(K-1):
        print i*(K**(C-1)) + i+1 +1,
    print
