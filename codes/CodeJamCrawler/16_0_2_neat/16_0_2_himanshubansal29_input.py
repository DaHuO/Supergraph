t=input()
for r in range(t):
    n=raw_input()
    c=0
    while(True):
        if(n.count("-")==0):
            break;
        c=c+1
        k=n.rfind("-")
        n=n[0:k+1]
        m=list(n)
        for i in range(k+1):
            if(n[i]=="+"):
                m[i]="-"
            else:
                m[i]="+"
        n=''.join(m)
    print "Case #"+str(r+1)+": "+str(c)
