
t=int(input())
for k in range(t):

    n=int(input())
    i=0
    a=[0]*10
    if(n==0):
        print('Case #{}: INSOMNIA'.format(k+1))
    else:
        count=0
        while(count<10):
            i+=1
            num=i*n
            

            while(num>0):
                d=num%10
                if(a[d]!=1):
                    a[d]=1
                    count+=1
                    
                num=int(num/10)
        print("Case #{}: {}".format(k+1,i*n))

   
