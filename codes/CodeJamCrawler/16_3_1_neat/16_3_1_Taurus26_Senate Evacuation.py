File=open("A-large.txt",'w')

L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

T=int(raw_input())
for t in range(T):
    N=int(raw_input())
    P=[int(s) for s in raw_input().split()]
    p=P[:]
    for i in range(N):
        if p[i]==max(p):
            m=i
            p[i]=0
            break
    for i in range(N):
        if p[i]==max(p):
            n=i
            break
    l=[L[m],L[n]]
    y=[]
    for i in range(P[m]-P[n]):
        y.append(L[m])     
    for i in range(N):
        if i==m or i==n:
            continue
        else:
            for j in range(P[i]):
                y.append(L[i])
    for i in range(P[n]):
        y.append(''.join(l))
    y=' '.join(y)
    print >> File, "Case #%d: %s" %(t+1,y)
File.close()
        
