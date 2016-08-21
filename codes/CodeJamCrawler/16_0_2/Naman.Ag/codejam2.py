t=input()
for k in range(0,t):
    s=list(raw_input());
    l=len(s);
    ans=0;
    while True:
        i=0
        f=0
        pos1=-1
        pos2=-1
        for i in range(0,l):
            if s[i]=='+':
                pos1=i;
            else:
                break;
        if pos1==l-1:
            break;
        for i in range(0,pos1+1):
            s[i]='-';
        if pos1!=-1:
            ans=ans+1;
        for i in range(0,l):
            if s[i]=='-':
                s[i]='+';
            else:
                break;
        ans=ans+1;
    print 'Case #'+str(k+1)+': '+str(ans);
