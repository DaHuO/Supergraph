t=input()
for i in xrange(t):
    a=[]
    s=raw_input().strip()
    l=len(s)
    for j in xrange(l):
        a.append(s[j])
    ans=0
    for j in xrange(l):
        if j==l-1 and a[j]=='-':
             ans+=1
             for k in xrange(j+1):
                a[k]='+'
             j=0
        elif a[j]=='-'and a[j+1]=='+':
            ans+=1
            for k in xrange(j+1):
                a[k]='+'
            j=0
        elif a[j]=='+' and j==l-1:
            break
        elif a[j]=='+' and a[j+1]=='-':
            ans+=1
            for k in xrange(j+1):
                a[k]='-'
            j=0

    print "Case #%d:"%(i+1),ans
    del a