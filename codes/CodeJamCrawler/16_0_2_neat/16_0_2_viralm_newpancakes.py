t=input()
for kk in range(0,t):
    d={}
    s=raw_input()
    n=len(s)
    z="Case #"+str(kk+1)+":"
    ar=[0]*(n+10)
    ar[0]=0
    for i in range(1,n+1):
        t1='-'*i
        t2='+'*i
        if s[0:i]==t1:
            ar[i]=1
        elif s[0:i]==t2:
            ar[i]=0
        elif((i-2>=0) and (s[i-1]=='-') and (s[i-2]=='-')):
            ar[i]=ar[i-1]
        else:
            if s[i-1]=='+':
                ar[i]=ar[i-1]
            else:
                ar[i]=ar[i-1]+2
    print z,ar[n]
