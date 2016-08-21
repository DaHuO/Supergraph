#!/usr/bin/python3
import re


def solve( i, N, not_seen = '1234567890' ):
	not_seen = re.sub( '[{0}]'.format( i*N ), '', not_seen )
	
	if ( len( not_seen ) == 0 ):
		return ( i*N )

	return solve( i + 1, N, not_seen )

def Main():

	for testCase in range( 1, int( input() ) + 1 ):
		N = int( input() )
		print( 'Case #{0}: {1}'.format( testCase, 'INSOMNIA' if ( N == 0 ) else solve( 1, N ) ) )

# End Main

if __name__ == '__main__':
	Main()