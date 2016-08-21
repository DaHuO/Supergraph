def topple(t):
    if t=='+':
        return '-';
    elif t=='-':
        return '+';
def codejam2(l):
    s=list(l);
    j=0;    
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            s[0:i]=map(topple,s[0:i]);
            j+=1;
    if s[0]=='-':
        s=map(topple,s[0:len(s)]);
        j+=1;
    return j;
n=input();
I=[];
for k in range(n):
    I.append(raw_input());
k=1;
while k<=n:
    print 'Case #'+str(k)+': '+str(codejam2(I[k-1]));
    k+=1;
