import math
def atkin(nmax):
    
    is_prime = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes
pri = atkin(65536)

def isPrime(m):
    
    
    for m2 in pri:
        if(m%m2 == 0):
            x1 = [m2,False]
            return x1
        
    x1 = [0,True]
    return x1
for t in range(int(input())):
    print("Case #1:")
    N,J = map(int,input().split())
    start = int("1" + "0"*(N-2) + "1",2)
    end = int("1" + "0"*N , 2)
    ct = 0
    for n in range(start, end,2):
        ls = []
        b = bin(n)[2:]
        f = True
        for c in range(2,11):
            h = isPrime(int(b,c))
            if h[1]:
                f = False
                break
            ls.append(h[0])
        if f:
            
            s = ""
            for i in ls:
                s += " " + str(i)
            s = str(b) + s
            print(s)
            ct+=1
            if(ct == J):
                
                break
