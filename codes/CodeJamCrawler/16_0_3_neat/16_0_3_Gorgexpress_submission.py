import itertools
import re
import math

primes = [2, 3, 5, 7, 11, 13, 17]

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
    
def isJamCoin(coin):
    if coin[0] != 1 or coin[len(coin) - 1] != 1:
        return None
    coin = coin[::-1]
    divisors = []
    for base in range(2, 11):
        value = 0
        exp = 0
        for digit in coin:
            if digit == 1:
                value += base ** exp
            exp += 1
        for prime in primes:
            if value % prime == 0:
                divisors.append(prime)
                break
        else:
            return None
    return divisors

out = open("A.out", "w")
with open("A.in") as f:
    T = int(f.readline())
    N, J = (int(num) for num in f.readline().split())
    out.write("Case #{}:\n".format(T))
    for perm in itertools.product([0,1], repeat=N - 2):
        lst = list(perm)
        lst = [1] + lst + [1]
        divisors = isJamCoin(lst)
        if(divisors != None):
            out.write("{} {}\n".format(re.sub('[\[\], ]', '', str(lst)), re.sub('[\[\],]', '', str(divisors))))
            J -= 1
            if(J == 0):
                break
        
    
out.close()