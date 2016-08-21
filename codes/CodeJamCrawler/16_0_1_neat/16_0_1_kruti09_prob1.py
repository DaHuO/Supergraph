T= int(input())
j=0
while(T>0):
    j+=1
    d=set()
    N= int(input())
    i=1
    s=0
    if N==0:
        c="INSOMNIA"
    else:  
        while(True):
            a=N*i
            c=a
            while(a!=0):
                b=a%10
                a=a//10
                d.add(b)
            s=sum(d)
            i=i+1  
            if s==45 and 0 in d:
                break
    print("Case #{}: {}".format(j,c))   
    T=T-1           