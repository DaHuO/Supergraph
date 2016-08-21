import sys

def sleep(N):
    if N == 0:
        return 'INSOMNIA'
    
    l = set()
    i = 1

    orig = N

    while l != set(['1','2','3','4','5','6','7','8','9','0']):
        s = str(N)
        for x in s:
            l.add(x)

        prev = N
        N = (i+1)*orig
        i += 1

    return prev 
    

        

T = int(sys.stdin.readline())
for case in xrange(T):
    N = int(sys.stdin.readline())
    print 'Case #%d: %s' % (case + 1, str(sleep(N)))
