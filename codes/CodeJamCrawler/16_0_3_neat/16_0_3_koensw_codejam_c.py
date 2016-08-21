import itertools
import math

T = raw_input()
N = int(raw_input())
J = int(raw_input())

MAXN = int(1e9)

def find_divisor(a):
    for i in range(2, int(math.sqrt(a)+1)):
        if (a % i) == 0: return i
    
    return -1

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n):
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
    else:
        return not any(_try_composite(a, d, n, s) for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022))
    

print "Case #1:"
cnt = 0
for seq in itertools.product("01", repeat=N):
    if seq[0] != '1' or seq[-1] != '1': continue

    ccnt = 0
    for i in range(2,11):
        k = int("".join(seq), i)
        if not is_prime(k): ccnt = ccnt + 1
     
     
    if ccnt == 9: 
        ans = []

        for i in range(2,11):    
            k = int("".join(seq), i)
            ans.append(find_divisor(k))
        
        cnt = cnt + 1
        print "".join(seq),
        for i in ans:
            print i,
        print
        
        if cnt == J: break
        
    
