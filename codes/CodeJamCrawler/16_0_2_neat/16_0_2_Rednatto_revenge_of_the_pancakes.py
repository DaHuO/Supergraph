#!/usr/bin/python

import sys

def pancake( s, t ):
    if ( len(s)==0 ):
        return 0
    return pancake( s[1:], s[0] ) + ( 0 if ( s[0]==t ) else 1 )

    

t = int( sys.stdin.readline() )
data = [ x.strip()[::-1]  for x in sys.stdin.readlines() ]
for i in range( t ):
    print( "Case #{}: {}".format( i+1, pancake(data[i],'+')) )



