#!/usr/bin/python

import sys
from random import *


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = rwh_primes( 10**4 )

def check_edges( coin ):
    return ( ( coin[0]=='1' ) and ( coin[-1]=='1' ) )
    
def to_deci( coin, base ):
    num = 0
    for i,c in enumerate(coin[::-1]):
        if ( c == '1' ):
            num = num + base**i

    return num

def check_divisor( num, div ):
    if ( div == num ):
        return False
    return ( num % div ) == 0

def check_coin( coin, divisors, N ):
    
    if ( not check_edges( coin ) ):
        return False
    if ( not len(coin) == N ):
        return False

    for i in range( 2,11 ):

        if ( divisors[i] <= 1 ):
            return False

        num = to_deci( coin, i )
        if ( not check_divisor( num, divisors[i] ) ):
            return False

    return True

def get_rand_coin( N ):

    return '1' + "".join([ ('0' if (randint(0,1)==0) else '1') for i in range(N-2)]) + '1'

def get_divisor( num ):
    for i in primes:
        if ( num % i == 0 ):
            return i

    return num

def generate_coins( N, J ):
    
    coinset = set()
    nfound = 0
    while ( nfound < J ):
        coin = get_rand_coin( N )
        if ( coin in coinset ):
            continue
        #print( "maybe:", coin )

        divisor = dict()
        for i in range( 2, 11 ):
            divisor[i] = get_divisor( to_deci(coin,i) )
            if divisor[i] == 1:
                del divisor[i]
                break
        if ( len(divisor) != 9 ):
            continue

        if ( check_coin( coin, divisor, N ) ):
            coinset.add( coin )
            print coin, divisor[2], divisor[3], divisor[4], divisor[5], divisor[6], divisor[7], divisor[8], divisor[9], divisor[10] 
            nfound = nfound + 1



t = int( sys.stdin.readline().strip() )
[ N, J ] = [ int(x) for x in sys.stdin.readline().strip().split() ]
print "Case #1:"
generate_coins( N, J)

