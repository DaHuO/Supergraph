import sys

def ans(s):
    l = []
    N = len(s)
    if s == '+'*N:
        return 0

    if s == '-'*N:
        return 1

    if N == 1:
        if s == '-':
            return 1
        else:
            # Don't really need this...
            return 0

    i = 1
    count = 0
    a = s[0]
    
    while i < len(s):
        if s[i] != a:
            count += 1
            a = s[i]
        i += 1

    if s[N-1] == '-':
        count += 1

    return count
        
        



def complement(a):
    if a == '0':
        return '1'

    else:
        return '0'





def pancake(s):
    l = []
    N = len(s)
    if s == '+'*N:
        return 0

    if s == '-'*N:
        return 1

    if N == 1:
        if s == '-':
            return 1
        else:
            # Don't really need this...
            return 0
        
    for i in s:
        if i == '-':
            l.append('0')
        else:
            l.append('1')

    count = 0

    while l != ['1']*N:
        if l == ['0']*N:
            return count + 1
        #print l
        a = l[0]
        for i in xrange(N):
            if l[i] != a:
                break

        for j in xrange(i):
            l[j] = complement(a)
        count += 1
        
    return count




T = int(sys.stdin.readline())
for case in xrange(T):
    s = sys.stdin.readline().strip('\n')
    print 'Case #%d: %d' % (case + 1, ans(s))#pancake(s))
    



            
            
