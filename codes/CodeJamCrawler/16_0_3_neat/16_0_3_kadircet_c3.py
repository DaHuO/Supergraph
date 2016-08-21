import gmpy

primes = []
n=gmpy.mpz(16)
j=50

def calcprimes(N):
    primes.append(gmpy.mpz(2))
    i=gmpy.mpz(3)
    while(i<=N):
        if gmpy.is_prime(i)!=0:
            primes.append(i)
        i+=2

def is_prime(x, k):
    y=0
    if k!=2:
        b=gmpy.mpz(1)
        while x>0:
            if x%2==1:
                y+=b
            x/=2
            b*=k
        x=y
    if(gmpy.is_prime(x)!=0):
        return 0
    for i in primes:
        if x%i==0:
            return i
        if i*i>x:
            break
    return 0

def base2(x):
    res=""
    while x>0:
        res+=str(x%2)
        x/=2
    return res[::-1]

calcprimes(10**7)
i=gmpy.mpz(0)
M=2**(n-2)
while(i<M):
    x=2*i+1+2**(n-1)
    divs=[]
    for k in range(2,11):
        y=is_prime(x, k)
        if y==0:
            break
        divs.append(y)
    else:
        j-=1
        print base2(x),
        for x in divs:
            print x,
        print
    if j==0:
        break
    i+=1
