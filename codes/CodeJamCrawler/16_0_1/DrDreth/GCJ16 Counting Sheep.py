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

inFname = "CS.in"
outFname = "CS.out"

#data = [ r.randrange( 0, int( 10e6 ) ) for i in xrange( int( 10e6 ) ) ]
data = get_input( int )
results = []

for j,i in enumerate( data ):
    if i == 0:
        results.append( "INSOMNIA" )
        continue;
    s = set()
    count = 1
    while len( s ) != 10:
        temp = i * count
        count += 1
        s.update( list( str( temp ) ) )
    results.append( temp )

output_to_console( results )
output_to_file( outFname, results )