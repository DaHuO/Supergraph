# coding: utf-8
f = open('/Users/hashimototatsuya/Downloads/D-small-attempt0.in','r')
T = int(f.readline())
for t in range(T):
    K,C,S= map(int, f.readline().split())
    SS = [i+1 for i in range(S)]
    SSS = ''
    for i in xrange(S):
        SSS += ' ' + str(SS[i])

    print 'Case #%d:%s'%(t+1, SSS)

f.close()
