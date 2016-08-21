from pyprimes import is_prime
from pprint import pprint
import random

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def pollardRho(N):
        if N%2==0:
                return 2
        x = random.randint(1, N-1)
        y = x
        c = random.randint(1, N-1)
        g = 1
        while g==1:
                x = ((x*x)%N+c)%N
                y = ((y*y)%N+c)%N
                y = ((y*y)%N+c)%N
                g = gcd(abs(x-y),N)
        return g

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


def prime(n):
    if is_prime(n):
        return True, None
    else:
        #print 'checking factors', n
        return False, brent(n)


def process(bits, coins_to_output):
    result = []
    current_jamcoin = 2**(bits-1) + 1

    while len(result) < coins_to_output:
        jamcoin_str = bin(current_jamcoin)[2:]
        #print 'trying coin', jamcoin_str

        found_prime = False
        divisors = []
        for base in xrange(2, 11):
            interpreted_number = int(jamcoin_str, base)
            is_prime, divisor = prime(interpreted_number)
            if is_prime:
                found_prime = True
                break
            else:
                divisors.append(divisor)

        if not found_prime:
            result.append((jamcoin_str, divisors))
            print 'found coin'
        current_jamcoin += 2

    return result



number_of_cases = int(raw_input())
for case_number in xrange(1, number_of_cases+1):
    bits, coins_to_output = map(int, raw_input().split())

    result = process(bits, coins_to_output)

    print "Case #%d:" % (case_number, )
    for r in result:
        print r[0], ' '.join(map(str, r[1]))
    case_number += 1

#pprint(process(32, 500))