#!/usr/bin/env python
__author__ = "Thomas Kargul"

from math import sqrt
from itertools import count, islice

def coinJam():
	#not safe but inputs are guaranteed correct
	garbage1 = raw_input()
	realinput = raw_input()
	mylist = realinput.split()
	N = int(mylist[0]) #length of string
	J = int(mylist[1]) #find J different jamcoins

	#if it is a prime number, we want the number that divides it evenly
	def isPrime(n):
	    if n < 2: return 1 #not prime and will never happen since N > 2
	    for number in islice(count(2), int(sqrt(n)-1)):
	        if not n%number:
	        	#print "div number: {}".format(number)
	           	return number #not prime
	    return 0 #prime

	#if N = 4, then 1001, cycle between middle 1001 > 1011 > 1101 > 1111
	#so basically str = 1 + middle + 1 > then convert str to different base ints
	#then check if those ints are prime or not
	#if all bases 2-10 are NOT PRIME, then it is a jamcoin
	#fixedLength = 5
	#binaryN = "{:0{}b}".format(N, fixedLength)
	#print binaryN


	middleLength = N - 2
	#print ("middleLength: {}".format(middleLength))
	maxRange = (2 ** middleLength) - 1
	#print ("maxRange: {}".format(maxRange))
	middle = 0 #max value will be maxRange
	#print ("middle: {}".format(middle))
	Jcount = 0
	jamcoins = {} #k = jc, v = str(list of divisors)

	while Jcount < J and middle < maxRange:
		stringJC = "1" + "{:0{}b}".format(middle, middleLength) + "1"
		divisorList = []
		#convert to different base ints
		for b in range(2,11): 
			intJC = int(stringJC, b)
			divisor = isPrime(intJC)
			if divisor == 0: break
			else: divisorList.append(str(divisor))
		if len(divisorList) == 9: #was not prime in all bases
			jamcoins[stringJC] = " ".join(divisorList)
			Jcount += 1
		middle += 1


	print("Case #1:")
	for jamcoin in jamcoins:
		print("{} {}".format(jamcoin, jamcoins[jamcoin]))




	#print the 1001 followed by its DIVISORS for each base





if __name__ == '__main__':
	coinJam()