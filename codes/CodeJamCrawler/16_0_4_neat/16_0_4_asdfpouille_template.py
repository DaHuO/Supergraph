#!/usr/bin/python

import sys

		
def main():
	with open(sys.argv[1], 'r') as f:
		n = int(f.readline())
		lines = [f.readline() for i in xrange(n)]
	for i in xrange(n):

if __name__ == '__main__':
	main()
