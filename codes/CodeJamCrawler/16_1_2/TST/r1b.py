# coding: utf-8

f = open('/Users/hashimototatsuya/Downloads/B-small-attempt0 (1).in','r')

T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    G = ['' for i in range(2*N-1)]
    GG = [0 for i in range(2501)]
    
    for i in range(2*N-1):
        G[i] = map(int, f.readline().split())
    
    for i in range(2*N-1):
        for r in range(N):
            GG[G[i][r]] += 1

    print 'Case #%d:'%(t+1),
    for i in range(2501):
        if GG[i]%2 == 1:
            print i,
    print ''



f.close()