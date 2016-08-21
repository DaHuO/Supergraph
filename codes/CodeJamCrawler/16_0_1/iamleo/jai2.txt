t=int(input())
a=[]
for t in range(t):
    n=int(input())
    if(n==0):
        z='INSOMNIA'
    else:
        for i in range(10):
            a.append(i)
        x=n
        i=1
        while(len(a)>0):
            while(n>0):
                k=n%10
                if(a.count(k)==1):
                    del a[a.index(k)]
                n=int(n/10)
            i=i+1
            n=i*x
        z=n-x
    print('Case #',end='')
    print(t+1,end='')
    print(': ',end='')
    print(z)
