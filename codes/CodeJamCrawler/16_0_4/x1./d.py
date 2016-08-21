import math
import random
import sys
import time

"""
Problem D. Fractiles
"""

T = int( raw_input() )
kcs = []
for x in xrange( T ):
    kcs.append( map( int, raw_input().split() ) )

memo = {}

#----------------------------
def solv( q ):

    K = q[0]
    C = q[1]
    S = q[2]

    res = ''

    look_start = 0
    look_end   = 0

    if C == 1 or K == 1:
        look_start = 1
        look_end   = K
    else:
        look_start = 2
        look_end = K

    #print look_start, look_end

    if S <= ( look_end - look_start ):
        print "NG"
        res = "IMPOSSIBLE"
    else:
        if memo.has_key( (look_start, look_end) ):
            ans = memo[ (look_start, look_end) ]
        else:
            ans = " ".join( [ str( x ) for x in xrange( look_start, look_end + 1 ) ] )

        res = ans

    return res


#----------------------------

start = time.clock()

res = []
for q in kcs:
    res.append( solv( q ) )

i = 0
for r in res:
    i +=1
    print( "Case #{0}: {1}".format( i, r ) )

#end = time.clock()
#print end - start
sys.exit(0)
