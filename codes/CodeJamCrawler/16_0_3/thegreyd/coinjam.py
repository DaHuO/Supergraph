import itertools as it
import random

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def brent(N):
    if N%2==0:
            return 2
    y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:             
            x = y
            for i in range(r):
                    y = ((y*y)%N+c)%N
            k = 0
            while (k<r and g==1):
                    ys = y
                    for i in range(min(m,r-k)):
                            y = ((y*y)%N+c)%N
                            q = q*(abs(x-y))%N
                    g = gcd(q,N)
                    k = k + m
            r = r*2
    if g==N:
            while True:
                    ys = ((ys*ys)%N+c)%N
                    g = gcd(abs(x-ys),N)
                    if g>1:
                            break
     
    return g    

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

def check(binstring):
    #print("checking for ", binstring)
    for base in range(2,11):
        num = int(binstring,base)
        if(is_prime(num)):
            return False
    return True

def primefactors(n):
    limit = int(n ** .5) + 1
    for checker in _known_primes:
        #print(_known_primes[-1])
        if(checker > limit): 
            break
        while(n % checker == 0):
            return checker

    return(brent(n))    

def factors(binnum):
    l = []
    for base in range(2,11):
        num = int(binnum,base)
        f=primefactors(num)
        if(f==num or f==1):
            f=str(f)+"!!!!!"
        l.append(f)
    return l

for t in range(int(input())):
    arr = input().split()
    n,j = int(arr[0]), int(arr[1])
    print("Case #{}: ".format(t+1))
    
    for i in it.product("01",repeat=n-2):
        binnum = "{}{}{}".format("1","".join(i),"1")
        if(check(binnum)):
            l=factors(binnum)
            print(binnum,*l)
            j-=1
        if(j==0):
            break