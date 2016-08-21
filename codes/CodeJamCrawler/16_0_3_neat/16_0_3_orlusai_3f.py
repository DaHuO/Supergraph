# From https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test

from math import sqrt
from math import ceil

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
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

outFile = open("C-large-attempt0.out", "w")
print("Case #1:", file=outFile)

start = int(30*"0", 2)
end = int(30*"1", 2)

cnt = 0

for binRepresPart in range(start, end+1):
    binRepres = "1" + bin(binRepresPart)[2:].rjust(30, "0") + "1"

    resultStr = binRepres + " "

    stopped = False

    for i in range(2, 10):
        repres = int(binRepres, i)

        if is_prime(repres):
            stopped = True
            break

    if stopped:
        continue

    for i in range(2, 10):
            repres = int(binRepres, i)
            
            if(repres%2 == 0):
                resultStr += "2 "
##                input()
            else:
                for j in range(3, 10000000, 2):#ceil(sqrt(repres))+1, 2):
                    if(repres%j == 0):
                        resultStr += str(j) + " "
                        break
                if j>=10000000-3:
                    stopped = True

    i = 10
    repres = int(binRepres, i)
        
    if(repres%2 == 0):
        resultStr += "2"
    else:
        for j in range(3, 10000000, 2):
            if(repres%j == 0):
                resultStr += str(j)
                break
        if j>=10000000-3:
            stopped = True

    if not stopped:
        print(resultStr, file=outFile)
        cnt += 1
        if(cnt%10 == 0):
            print(cnt, binRepres)
        if(cnt==500):
            break

outFile.close()
