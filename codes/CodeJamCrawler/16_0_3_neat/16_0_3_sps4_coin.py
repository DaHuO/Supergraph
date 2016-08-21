from math import sqrt
#from sympy.ntheory import factorint

WIDTH = 32
COINT_COINT = 500

import numpy
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


primes = numpy.load("primes.txt.npy")

def factors(n):
    limit = sqrt(n)
    for p in primes:
        if n % p == 0:
            return p

        if p >= limit:
            return False


def check_valid_base(digits, base):
    sum3 = 0
    sum5 = 0
    sum7 = 0
    sum9 = 0
    sum11 = 0

    for (pos, bit) in enumerate(reversed(digits)):
        if bit:
            sum3 += pow(base, pos, 3)
            sum5 += pow(base, pos, 5)
            sum7 += pow(base, pos, 7)
            sum9 += pow(base, pos, 9)
            sum11 += pow(base, pos, 11)

    if sum3 % 3 == 0:
        return 3
    elif sum5 % 5 == 0:
        return 5
    elif sum7 % 7 == 0:
        return 7
    elif sum9 % 9 == 0:
        return 9
    elif sum11 % 11 == 0:
        return 11
    else:
        return False

    #return factors(sum)

def check_valid(bits):
    base_factors = []
    for base in range(2, 11):
        factor = check_valid_base(bits, base)
        if not factor:
            return False
        base_factors.append( factor )

    return base_factors

import itertools
result_file = open('out.txt', 'w')
print('Case #1:')
found_coins = 0
for num in itertools.product( [1,0], repeat=WIDTH - 2):
    bits = (1,) + num + (1,)
    #print bits
    factor = check_valid(bits)
    if factor:
        #print bits, factor
        coin = ''.join( str(x) for x in bits)
        divisors = ' '.join(str(x) for x in factor)
        print coin, divisors
        result_file.write(coin + ' ' + divisors + '\n')
        found_coins += 1

    if found_coins == COINT_COINT:
        break

result_file.close()

