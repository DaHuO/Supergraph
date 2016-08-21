from bitarray import bitarray
import sympy
from itertools import product
import time

def is_prime_or_not_v5(n):
    if sympy.isprime(n):
        return True, None
    else:
        i = 0
        e = int(n**0.5)+1
        while True:
            i += 1
            p = sympy.prime(i)
            if n % p == 0:
                return False, p
            if p>=e:
                return True, None
            if i >= 20000:
                # too large for this number
                return True, None

def is_jamcoin_v5(s):
    divisors = []
    for base in range(2,11):
        n = int(s, base)
        isp, div = is_prime_or_not_v5(n)
        if isp:
            return False, divisors
        divisors.append(div)
        
    return True, divisors

def get_jamcoins(n, j):
    m = int('1'*(n-1), 2)
    e = int('1'*(n-2), 2)
    i = 0
    jamcoins = []

    for g in product('01',repeat=30):
        s = '1' + ''.join(g) + '1'
        is_jamcoin, divisors = is_jamcoin_v5(s)
        if is_jamcoin:
            jamcoins.append((s, divisors))
            print s,
            for d in divisors:
                print d,
            print ''
            
            if len(jamcoins)>=j:
                break
        i += 1
    

def test():
    get_jamcoins(32,10)


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, j = [int(s) for s in raw_input().split(" ")]
        print "Case #{}:".format(i)
        get_jamcoins(n, j)

if __name__=='__main__':
    main()
