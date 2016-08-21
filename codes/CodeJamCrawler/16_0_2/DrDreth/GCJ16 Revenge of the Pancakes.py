#import random as r

def get_input( f = lambda x: x ):
    return map( f, raw_input( "Enter input:\n" ).splitlines()[1::] )

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

inFname = "RotP.in"
outFname = "RotP.out"

data = get_input( list )
results = []

def flip_sign( s ): return map( lambda x: "-" if x == "+" else "+", s )
def flip_order( s ): return s[::-1]
def flip( s ): return flip_sign( flip_order( s ) )

def lookup_solution( s ):
    if len( s ) == 1:
        return 0 if s[ 0 ] == "+" else 1
    elif s[-1] == "-":
        s = flip_sign( s )
        return 1 + lookup_solution( s[:-1:] )
    else:
        return lookup_solution( s[:-1:] )

for i in data:
    results.append( lookup_solution( i ) )

output_to_console( results )
output_to_file( outFname, results )