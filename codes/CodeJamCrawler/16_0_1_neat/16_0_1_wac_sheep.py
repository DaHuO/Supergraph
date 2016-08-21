import sys
inf = open( sys.argv[ 1 ] ) 
outf = open( 'out.txt', 'w' )
n = int( inf.readline().strip() )
for i in xrange( n ):
    m = inf.readline().strip()
    if( m == '0' ):
        outf.write( 'Case #' + str( i + 1 ) + ': ' + 'INSOMNIA\n' )
        continue
    seen = [ c for c in set( m ) ]
    m = int( m )
    j = 1
    k = m
    while( len( seen ) < 10 ):
        j += 1
        k = m * j
        seen += [ c for c in set( str( k ) ) if c not in seen ]
        #print str( k ) + ": " + str( sorted( seen ) )
    outf.write( 'Case #' + str( i + 1 ) + ": " + str( k ) + '\n' )

outf.close()
