t=int(raw_input())
for i in range(t):
    s=raw_input()
    l=list(s)
    n=0
    print "Case #"+`i+1`+":",
    while '-' in l:
        if l[0]=='+':
            l[0]='-'
            for k in range(1,len(l)):
                if l[k]=='+':
                    l[k]='-'
                else:
                    break
        else:
            l[0]='+'
            for k in range(1,len(l)):
                if l[k]=='-':
                    l[k]='+'
                else:
                    break
        n=n+1
    print `n`
