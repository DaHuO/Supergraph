t=int(raw_input())
ii=1
while t>0:
    n=int(raw_input())
    a=[int(x) for x in raw_input().split()]
    b=[]
    for i in range(n):
        b.append([a[i],i])
    s=""
    while 1:
        b.sort(reverse=True)
        ss=0
        #print(b)
        for i in b:
            ss+=i[0]
        #if b[0][0]>ss/2:
        #    print("NO")
        if b[0][0]!=b[1][0]:
            if b[0][0]>=2:
                b[0][0]-=2
                s+=chr(b[0][1]+65)*2+" "
            elif b[0][0]==1:
                b[0][0]=0
                s+=chr(b[0][1]+65)+" "
            elif b[0][0]==0:
                break
        else:
            if b[0][0]>=1:
                b[0][0]-=1
                b[1][0]-=1
                s+=chr(b[0][1]+65)
                s+=chr(b[1][1]+65)+" "
            elif b[0][0]==0:
                break
        
    
    s=s.split()
    if len(s[-1])==1:
        z=s[-2][-1]
        s[-2]=s[-2][:-1]
        s[-1]+=z
    s=' '.join(s)    
    print("Case #"+str(ii)+": "+str(s))
    ii+=1
    t-=1
