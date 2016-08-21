def isprime(n):
    if n < 2:
        return 0
    if n == 2:
        return 0
    if n%2==0:
        return 2
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return x
    return 0

t=int(input())
for w in range(t):
    n,k=map(int,input().split())
    print("Case #",end='')
    print(w+1,end='')
    print(":")
    minn=2**(n-1)+1
    maxn=(2**n)
    while k>0:
        #print(minn)
        for j in range(minn,maxn):
            if k<=0:
                break
            #print(j)
            f2=isprime(j)
            if f2>0:
                binary="{0:b}".format(j)
                if int(binary)%10==0:
                    continue
                n3=int(binary,3)
                f3=isprime(n3)
                if f3==0:
                    continue
                n4=int(binary,4)
                f4=isprime(n4)
                if f4==0:
                    continue
                n5=int(binary,5)
                f5=isprime(n5)
                if f5==0:
                    continue
                n6=int(binary,6)
                f6=isprime(n6)
                if f6==0:
                    continue
                n7=int(binary,7)
                f7=isprime(n7)
                if f7==0:
                    continue
                n8=int(binary,8)
                f8=isprime(n8)
                if f8==0:
                    continue
                n9=int(binary,9)
                f9=isprime(n9)
                if f9==0:
                    continue
                n10=int(binary,10)
                f10=isprime(n10)
                if f10==0:
                    continue
                print(binary,f2,f3,f4,f5,f6,f7,f8,f9,f10)
                k=k-1
                continue
        minn=j+1

