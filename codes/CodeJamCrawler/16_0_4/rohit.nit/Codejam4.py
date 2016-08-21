t=input()
for i in xrange(t):
    k,c,s=map(int,raw_input().strip().split(' '))
    print "Case #%d:"%(i+1),
    if k==1 and s>=k:
        print "1",
    elif c==1 and s<k:
        print "IMPOSSIBLE",
    elif c==1 and s>=k:
        for j in xrange(k):
            print j+1,
    elif c!=1 and s<k-1:
        print "IMPOSSIBLE",
    elif c!=1 and s>=k-1:
        print "2",
        for j in xrange(1,k-1):
            ans=j*k + (j+2)
            print ans,
    print ""