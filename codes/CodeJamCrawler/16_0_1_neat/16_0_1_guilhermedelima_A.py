#!/usr/bin/python2

import sys

def append_num( N, digit ):
	num = str( N )

	for i in num:
		digit[ ord( i ) - ord( '0' ) ] = True
	


def solve(N):
	if N == 0:
		return 'INSOMNIA'

	digit = [ False for i in range(10) ]

	count = 1

	while( False in digit ):
		append_num( N*count, digit )
		count = count+1

	return str( N * ( count-1 ) )


def main():
	N = input()

	for k in range(N):
		X = input()

		sys.stdout.write('Case #' + str(k+1) + ': ')
		sys.stdout.write( solve(X) + '\n' )
		sys.stdout.flush()


if __name__ == '__main__':
	main()
