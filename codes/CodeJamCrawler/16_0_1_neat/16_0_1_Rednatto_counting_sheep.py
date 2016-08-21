#!/usr/bin/python

import sys

def count_sheep( n ):

    seen = set( )

    i = 1
    num = i * n
    while ( len( seen ) != 10 ):
        num = i * n
        for c in str( num ):
            seen.add( c )
        i = i+1

    return num

t = int( sys.stdin.readline() )
data = [ int(x) for x in sys.stdin.readlines() ]
for i in range( t ):

    if ( data[i] == 0 ):
        print( "Case #{}: INSOMNIA".format( i+1 ) )
    else:
        print( "Case #{}: {}".format( i+1, count_sheep(data[i])) )

