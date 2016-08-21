tc=int(raw_input())
for t in range(tc):
    n=int(raw_input())
    a=[0]*2501
    c=[0]*2501
    p=[0]*n
    index=0
    for i in range(2*n-1):
        p=map(int,raw_input().split())
        for k in p:
            a[k]=a[k]+1
    for j in range(1,2501):
        if a[j]%2!=0:
            c[index]=j
            index=index+1
    c=set(c)
    c=sorted(c)
    print "Case #"+str(t+1)+":",
    for p in c:
        if p!=0:
            print p,
    print ""        
    
