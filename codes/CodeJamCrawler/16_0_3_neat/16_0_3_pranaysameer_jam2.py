def fromDigits(digits, b):
    n = 0
    for d in digits:
        n = b * n + d
    return n
def primeCheck(num):
    for i in range(2,int(pow(num,0.5))):
        if(num%i==0):
            return i
    return -1
        
t=int(input())
for k in range(0,t):
    print("Case #"+str(k+1)+":")
    n=input().split()
    j=int(n[1])
    n=int(n[0])-1
    count=0
    lim1=pow(2,n)+1
    lim2=pow(2,n+1)
    for i in range(lim1,lim2):
        temp=bin(i)
        if(temp[n+2]=='0'):
            continue
        arr=[]
        nums=[]
        for m in range(2,n+3):
            arr.append(int(temp[m]))
        for m in range(2,11):
            nums.append(fromDigits(arr,m))
            flag=0
            primes=[]
        tot=len(nums)
        for m in range(0,tot):
            if(primeCheck(nums[m])==-1):
                flag=1
                break
            else:
                primes.append(primeCheck(nums[m]))
        if(flag==1):
            continue
        else:
            count+=1
            ll=len(primes)
            sr=""
            for kb in range(0,ll):
                sr=sr+" "+str(primes[kb])
            print( temp[2:n+3]+" "+sr)
            if(count==j):
                break


        
            
            
        
        
        
    
