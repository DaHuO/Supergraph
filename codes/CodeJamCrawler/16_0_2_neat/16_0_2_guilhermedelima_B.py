#!/usr/bin/python2

import sys

def solve( line ):
	count = 0 if line[0] == '+' else 1

	for i in range( 1, len( line ) ):
		if line[i] == '-' and line[i-1] != line[i]:
			count = count + 2

	return count


def main():
	T = input()

	for k in range(1, T+1):
		line = raw_input()

		sys.stdout.write( 'Case #' + str(k) + ': ' )
		sys.stdout.write( str( solve( line ) ) + '\n' )
		sys.stdout.flush()


if __name__ == '__main__':
	main()
