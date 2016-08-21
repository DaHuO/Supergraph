from random import randint
import sys
sys.stdout=open("c-large.out",'w')
print 'Case #1:'
N=32
J=500
def power(base,exp,mod):
    if exp==0:return 1
    if exp==1:return base
    if exp%2==0:return power(base*base%mod,exp/2,mod)
    return base*power(base*base%mod,exp/2,mod)%mod
def isPrime(n,k):
    if n==2:return True
    if n%2==0:return False
    d=n-1
    r=0
    while d%2==0:
        r+=1
        d/=2
    for i in xrange(k):
        a=randint(2,n-2)
        x=power(a,d,n)
        if x==1 or x==n-1:continue
        cont=False
        for i in xrange(r-1):
            x=x*x%n
            if x==1:return False
            if x==n-1:
                cont=True
                break
        if cont:continue
        return False
    return True
while J:
    string=[1]
    for i in xrange(N-2):string.append(randint(0,1))
    string.append(1)
    nums=[]
    ans=[]
    poss=True
    for base in xrange(2,11):
        num=0
        for i in xrange(N):
            num*=base
            num+=string[i]
        nums.append(num)
        if isPrime(num,40):
            poss=False
            break
    if poss:
        J-=1
        for i in nums:
            if i%2==0:ans.append(2)
            else:
                for j in xrange(3,1000,2):
                    if i%j==0:
                        ans.append(j)
                        break
        if len(ans)<9:
            J+=1
            continue
        print ''.join(map(str,string)),
        for i in ans:
            print i,
        print
sys.stdout.close()
                    
        
