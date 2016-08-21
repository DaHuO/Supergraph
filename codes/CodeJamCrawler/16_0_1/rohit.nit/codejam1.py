t=input()
for i in xrange(t):
    s=raw_input().strip()
    s1=s[0]
    l=len(s)
    for j in xrange(1,l):
        if s[j]>=s1[0]:
            s1=s[j]+s1
        else:
            s1=s1+s[j]
    print "Case #%d:"%(i+1),s1