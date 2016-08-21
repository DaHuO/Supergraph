T = input()

for t in xrange(1,T+1):
    n = input()
    p = map(int,raw_input().split())
    print "Case #%d:"%(t),
#    print p,
    chk = True
    while True:
        if n == 2:
            break
        if sum(p) == n:
            break
        mx = max(p)
        ix = p.index(mx)
        p[ix] -= 1
        print chr(ord('A')+ix),
    if n == 2:
        print 'AB ' * p[0] 
        continue
    for i in xrange(n-2):
        print chr(ord('A')+i),
    print chr(ord('A')+n-2) + chr(ord('A')+n-1)
