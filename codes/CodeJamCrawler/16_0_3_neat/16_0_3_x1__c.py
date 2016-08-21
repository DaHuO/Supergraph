import math
import random
import sys
import time

"""
Problem C. Coin Jam
"""

T = int( raw_input() )
nj = map( int, raw_input().split() )
N = nj[0]
J = nj[1]

#----------------------------
def is_prime( q, k=50 ):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1

    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def devisor( v ):
    if v & 1 == 0:
        return 2
    #mx = min( sys.maxint, v )
    mx = 1000
    for x in xrange( 3, mx, 2 ):
        if v % x == 0:
            return x
    return None

#----------------------------
def solv( N, J ):

    x0 = [ "0" for _ in xrange(N) ]
    x0[0] = "1"
    x0[-1] = "1"

    x1 = [ "1" for _ in xrange(N) ]

    x0s = "".join( x0 )
    x1s = "".join( x1 )

    start_x = int( x0s, 2 )
    end_x = int( x1s, 2 )

    #print start_x, end_x
    jams = {}
    for x in xrange( start_x, end_x, 2 ):
        s = format( x, 'b' )
        jams = calc( J, s, jams )

        if len( jams ) == J:
            break
    return jams


def calc( J, sj, jams = {} ):

    #print sj
    devs = []
    for b in xrange( 2, 11 ):
        v = int( sj, b )
        if is_prime( v ):
            break
        d = devisor( v )
        if d is None:
            break
        devs.append( d )

    if len( devs ) == 9:
        jams[sj] = devs

    return jams


#----------------------------

start = time.clock()

res = solv( N, J )

print( "Case #1:" )

for k, v in res.items():
    dv = " ".join( map( lambda x: str(x), v ) )
    print( "{0} {1}".format( k, dv ) )


#end = time.clock()
#print end - start
sys.exit(0)
