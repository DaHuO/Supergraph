# coding: utf-8
import sys
f = open('/Users/hashimototatsuya/Downloads/A-large (1).in','r')

T = int(f.readline())

for t in range(T):
    S = f.readline()
    w = S[0]
    lens = len(S)
    k = ''
    for i in xrange(1,lens):
        if ord(S[i]) >= ord(w[0]):
            k = S[i] + w
        else:
            k = w + S[i]
        w = k
    sys.stdout.write('Case #%d: %s'%(t+1,w))
#print 'Case #%d: %s'%(t+1,w)

f.close()

