import math
#import time
#import itertools as it

def get_input( f = lambda x: x ):
    return map( f, raw_input( "Enter input:\n" ).splitlines()[1::] )

def get_multiline_input( s ):
    data = raw_input().splitlines()
    return [ data[i+1:i+1+s] for i in xrange( 0, s * int( data[ 0 ] ), s ) ]

def get_variable_line_input():
    data = raw_input().splitlines()
    retval, cache = [], []
    for i in data:
        if i.isdigit():
            if len( cache ):
                retval.append( cache )
                cache = []
            else:
                continue
        else:
            cache.append( i )
    retval.append( cache )
    return retval

def get_file_input( fname, fn = lambda x: x ):
    with open( "D:\\Python Projects\\Google Code Jam Inputs\\" + fname ) as f:
        data = map( fn, f.readlines()[1::] )
    return data

def output_to_file( fname, inData ):
    inData.reverse()
    ind = 0
    with open( "D:\\Python Projects\\Google Code Jam Outputs\\" + fname, "w" ) as f:
        while inData:
            ind += 1
            f.write( "Case #" + str( ind ) + ": " + str( inData.pop() ) + "\n" )

def output_to_console( indata ):
    for i in xrange( len( indata) ):
        print "case #" + str( i + 1 ) + ": " + str( indata[ i ] )

inFname = "TKW.in"
outFname = "Tb.out"

#f = lambda x: map( lambda y: int( y ), x.split() )

data = get_multiline_input( 2 )
results = []

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha = {}
for a,b in enumerate( alphabet ):
    alpha[ a ] = b

for i in data:
    case = map( int, i[ 1 ].split() )
    plan = []
    while sum( case ) != 0:
        prop = map( lambda x: float( x ) / float( sum( case ) ), case )
        maxvals = [ n for n,m in enumerate( prop ) if m == max( prop ) ]
        if len( maxvals ) > 2:
            maxvals = maxvals[0:2]
        elif len( maxvals ) == 1:
            maxvals.append( maxvals[ 0 ] )
        absmax = prop.index( max( prop ) )
        temp = case[::]
        for val in maxvals:
            temp[ val ] -= 1
        tempprop = map( lambda x: float( x ) / float( sum( temp ) ) if sum( temp ) != 0 else 0, temp )
        if len( filter( lambda x: x > 0.5, tempprop ) ) > 0:
            temp = case[::]
            temp[ absmax ] -= 1
            maxvals = [ absmax ]
            tempprop = map( lambda x: float( x ) / float( sum( temp ) ) if sum( temp ) != 0 else 0, temp )
            if len( filter( lambda x: x > 0.5, tempprop ) ) > 0:
                raise ValueError
        plan.append( maxvals )
        case = temp

    temp = map( lambda x: map( lambda y: alpha[ y ], x ), plan )
    temp = map( lambda x: reduce( lambda y,z: y + z, x ) + " ", temp )
    temp = reduce( lambda x, y: x + y, temp )
    results.append( temp[:-1] )

output_to_console( results )
output_to_file( "SELarge.txt", results )