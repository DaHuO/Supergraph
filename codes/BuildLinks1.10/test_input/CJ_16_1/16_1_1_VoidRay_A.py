import sys

def last(s):
    lastword = s[0]
    for i in xrange(1, len(s)):
        first = s[i]
        #print i, lastword, first
        if s[i] >= lastword[0]:
            lastword = s[i] + lastword 


        else:
            lastword = lastword + s[i]
        

        #first = s[i]
    return lastword






T = int(sys.stdin.readline())
for i in xrange(T):
    a = sys.stdin.readline()
    #print a
    print 'Case #%d: %s' % (i + 1, last(a))
    
