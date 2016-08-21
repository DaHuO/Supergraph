t=input()
l=1
while(l<=t):
    s1=raw_input()
    s=s1[0]
    for i in s1[1:]:
        if i>=s[0]:
            s=i+s
        else:
            s=s+i
    print "Case #%s:" % (l),
    print s
    l=l+1