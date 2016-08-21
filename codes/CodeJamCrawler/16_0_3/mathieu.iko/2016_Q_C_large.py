import sys
import numpy
import math
import random

N = 32
J = 500

random.seed()

coins_seen = []
divisors_seen = []


DEBUG=True if len(sys.argv) > 1 else False
def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)


def coinjam():
    """
        Returns a CoinJam with 'N' bits, having '1' as first and last digit
    """
    global N, coins_seen
    while True:
        coin = '1' + numpy.base_repr(random.randint(0, 1<<N-2)).zfill(N-2) + '1'
        if coin not in coins_seen:
            coins_seen.append(coin)
            yield coin
#    for i in range(1 << N-2):
#        yield '1'+ numpy.base_repr(i,2).zfill(N-2) +'1'


def primes(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


all_primes = primes(int(math.sqrt(1<<(N-2)))+1)


def divisor(n, base):
    global divisors_seen
    sqrt = int(math.sqrt(n))+1
    for x in all_primes:
        rep = int(numpy.base_repr(x,base), base)
        if n % rep == 0 and rep not in divisors_seen:
            divisors_seen.append(rep)
            return rep
        if x > sqrt:
            return 1
    else:
        return 1



print("Case #1:")

while True:
    coin = next(coinjam())
    divisors = []
    divisors_seen = []
    for n,b in [(int(coin, base), base) for base in range(2, 11)]:
        div = divisor(n,b)
        if div == 1:
            break
        else:
            divisors.append(div)
    else:
        print(coin, *divisors)
        J -= 1
        if not J:
            sys.exit(0)

