t=int(raw_input())
for k in range(0,t):
    n=int(raw_input())
    x=raw_input().split()
    y=[]
    p=0
    for i in range(0,n):
        x[i]=int(x[i])
        y.append(i)
        p=p+x[i]
    sol=""
    while(p>0):
        for j in range(0,n-1):
            for i in range(0,n-1):
                if(x[i]<x[i+1]):
                    temp=x[i]
                    temp1=y[i]
                    x[i]=x[i+1]
                    y[i]=y[i+1]
                    x[i+1]=temp
                    y[i+1]=temp1
        x[0]=x[0]-1
        if(p==n and n%2!=0):
            sol=sol+str(chr(y[0]+65))+" "
            p=p-1
        else:
            if(x[1]>0 and n>1):
                x[1]=x[1]-1
                p=p-2
                sol=sol+str(chr(y[0]+65))+str(chr(y[1]+65))+" "
            else:
                p=p-1
                sol=sol+str(chr(y[0]+65))+" "
    print "Case #"+str(k+1)+": "+sol
        
        
    
    
    
        
