import sys

T = int(sys.stdin.readline())

for it in xrange(T):
    n = int(sys.stdin.readline())
    x = 0

    print "Case #%d:" % (it + 1),
    
    if n == 0:
        print 'INSOMNIA'
        continue
        
    s = set()
    while len(s) < 10:
        x += 1
        s = s.union(set(list(str(n * x))))
    print x * n