import sys
import time

"""
"""
T = int( raw_input() )
ts = []
for i in xrange( T ):
    ts.append( int( raw_input() ) )

#----------------------------
start = time.clock()

res = []
for N in ts:
    if N == 0:
        res.append( "INSOMNIA" )
    else:
        s = set([])
        i = 0
        ans = 0
        while len( s ) < 10:
            i = i + 1
            ans = N * i
            ds = set( list( str( ans ) ) )
            if s >= ds:
                continue
            s = s.union( set(ds) )
            #for x in ds:
            #    s.add( x )

        if len( s ) == 10:
            res.append( str( ans ) )

i = 0
for r in res:
    i = i + 1
    print( "Case #{0}: {1}".format( i, r ) )

#end = time.clock()
#print end - start
sys.exit(0)
