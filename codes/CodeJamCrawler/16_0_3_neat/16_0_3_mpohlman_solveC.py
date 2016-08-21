#!/usr/bin/env python
import numpy
from random import random

debug=0

import numpy
def primesfrom3to(n):
	""" Returns a array of primes, 3 <= p < n. From http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
	sieve = numpy.ones(n/2, dtype=numpy.bool)
 	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = False
	return 2*numpy.nonzero(sieve)[0][1::]+1

def compute(N,J):
	jamCoinDictionary={}
	primes = primesfrom3to(2L**16)
	while len(jamCoinDictionary) < J:
		guess='1'+repr([str(int(random()>0.5)) for x in range(N-2)]).replace(",","").replace("[","").replace("]","").replace(" ","").replace("'","")+'1'
		#print 'guess:',guess
		divisors=[]
		for base in range(2,11):
			flag=0
			#print 'base:',base
			number=int(guess,base)
			#print 'number:',number
			for prime in primes:
				if prime < number and number%prime == 0:
					divisors.append(prime)
					#print number,prime,number%prime
					flag=1
					break
		if (len(divisors)==9) and guess not in jamCoinDictionary.keys():	
			jamCoinDictionary[guess]=divisors
	return jamCoinDictionary

def solve(infilename):
	infile=open(infilename,'r')
	line=infile.readline()
	T=int(line)
	if debug > 0:
		print 'T:',T
	#iterate
	for index in range(T):
		[N,J]=[int(i) for i in infile.readline().split()]
		if debug > 0:
			print 
			print 'N,J:',N,J
		jamCoinDictionary=compute(N,J)
		print 'Case #%(index)d:' % {"index":index+1}
		for coin in jamCoinDictionary:
			print '%(coin)s %(divisors)s' % {"coin":coin,"divisors":repr(jamCoinDictionary[coin]).replace(",","").replace("[","").replace("]","")}
	infile.close()
	return



if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		solve(sys.argv[1])
	else:
		solve('C-example.in')
