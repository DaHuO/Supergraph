t=int(raw_input())
jj=1
while t>0:
    n=int(raw_input())
    r=0
    a=[0]*10
    for i in range(1000):
        x=(i+1)*n
        while x>0:
            a[x%10]=1
            x=x/10
        p=0
        
        for j in range(10):
            if a[j]==0:
                p=1
        if p==0:
            r=(i+1)*n
            break
    if r!=0:    
        print("Case #"+str(jj)+": "+str(r))
    else:
        print("Case #"+str(jj)+": "+"INSOMNIA")
    jj+=1    
    t-=1
