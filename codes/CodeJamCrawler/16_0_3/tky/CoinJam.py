# Google code jam coin jam || python3

def isNewPrime(m,prime,primesum):
    out = True
    for i in range(0,len(prime)-1):
        if prime[i]**2 > m:
            break
        while (primesum[i]<m):
            primesum[i] += prime[i]
        if primesum[i] == m:
            out = False
            break
    return(out, primesum)

def calcPrimes(M,primes,primesum): # append prime numbers up to 'M' to seed 'prime'
    m = max(primes);
    while (m <= M):
        m += 1
        flag, primesum = isNewPrime(m,primes,primesum)
        if flag:
            primes = primes + [m]
            primesum = primesum + [m]
    return(primes,primesum)
    

def isLazyPrime(numstr,b,primes):
    x = int(numstr,b)
    out = True
    for y in primes:
        if y**2 >= x:
            break
        if x%y == 0: # ah ... cannot use int here with large numbers
            out = False
            break
    return(out,y)

def buildCoinString(num,N):
    out = '1'
    for j in range(N-3,-1,-1):
        if (num//2**j) == 1:
            out += '1'
        else:
            out += '0'
        num = num - (num//2**j)*2**j
    out += '1'
    return(out)

# start with some pre-calculated prime numbers
M = 1000
primes, primesum = calcPrimes(M,[2],[2])
       
T = int(input()) # read number of cases from stdin

for j in range(1,T+1):
    
    N, J  = [int(s) for s in input().split(" ")]

    print("Case #{}:".format(j))

    # may adjust max number according to log prime density
    M = 10000
    primes, primesum = calcPrimes(M,primes,primesum)

    i = 0
    found = 0
    while True:
        coin = buildCoinString(i,N)
        isPrime = False
        div = []
        # check if number is prime in any basis
        for b in range(2,11):
            isPrime, y = isLazyPrime(coin,b,primes)
            if isPrime:
                break            
            div.append(y)
            
        # found another jam coin
        if isPrime == False:
            outstring = ''
            for ii in range(0,len(div)):
                outstring = outstring + " {}".format(div[ii])
            print("{}{}".format(coin,outstring)) # jam coin result output
            found += 1

        # done ?
        if found == J:
            break

        i += 1

        # could not find required number of jam coins; write a warning
        if i >= 2**(N-1):
            print("Failure ; need larger set of prime numbers.")
            break

        
