#!/usr/bin/python3

def getOriginalArtworkPosition( n, K, C ):
	if ( C == 1 ):
		return n

	return ( n - 1 )*( K** ( C - 1 ) ) + getOriginalArtworkPosition( n, K, C - 1 )

def Main():

	for testCase in range( 1, int( input() ) + 1 ):
		K, C, S   = [ int( num ) for num in input().split() ]
		positions = [ str( getOriginalArtworkPosition( x, K, C ) ) for x in range( 1, K + 1 ) ]
		print( 'Case #{0}: {1}'.format( testCase, ' '.join( positions ) if len( positions ) <= S else 'IMPOSSIBLE' ) )

# End Main

if __name__ == '__main__':
	Main()