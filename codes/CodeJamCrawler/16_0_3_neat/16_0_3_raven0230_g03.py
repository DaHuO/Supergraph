from bisect import bisect_left

def numbase(coin, n):
    global N
    value = 0
    for i in range(N):
        value += coin[i] * pow(n,(N-1-i))
    return value

def is_prime(n):
    if n <= 33333334:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    for f in range(31627, limit, 6):
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
        
def genCoin(i, coin):
    global count
    global N
    global J
    if (count >= J): return
    if (i == N-1):
        curV = []
        for j in range(2,11):
            value = int(numbase(coin,j))
            prime = is_prime(value)
            if (prime): return
            else: curV.append(value)
        count += 1
        print("".join(list(map(str,coin))), end="")
        for j in curV:
            for k in range(2,33333335):
                if j%k == 0:
                    print(" {}".format(k),end="")
                    break
        print()
        return
    coin[i] = 0
    genCoin(i+1, coin)
    coin[i] = 1
    genCoin(i+1, coin)
    return

N = 16
J = 50
__primes  = sieve_for_primes_to(33333334)
count = 0
coin = [0]*N
coin[0] = coin[N-1] = 1
print("Case #1:")
genCoin(1,coin)
