t=int(input())
for _ in range(t):
    n=int(input())
    if(n==0):
       ans='INSOMNIA'
       print('Case #{}: {}'.format(_+1,ans))
    else:
        j=1
        a=set()
        while(1):
            num=n*j
            m=num
            while(num>0):
                d=num%10
                a.add(d)
                num=int(num/10)
            j+=1
            if(len(a)==10):
                break
        print('Case #{}: {}'.format(_+1,m))
