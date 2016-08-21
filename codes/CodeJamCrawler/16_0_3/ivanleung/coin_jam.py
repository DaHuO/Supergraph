import sys
import itertools
import math
from collections import defaultdict

def findNonTrivialDivisor(num):
	#print "findNonTrivialDivisor(",num,")"
	#print "findNonTrivialDivisor(",num,")",int(math.sqrt(num))
	for i in range(2, int(math.sqrt(num))):
		if num % i == 0:
			return i
	return -1

def findJamCoin(N, J):
	# N is length of jamcoin
	# J is how many jamcoins to find...

	#base str
	found = 1;
	for x in map(''.join, itertools.product('01', repeat=N-2)):
		#generate jamcoin
		jamcoin = "1"+x+"1"
		nonTrivials = validateJamCoin(jamcoin)
		if -1 in nonTrivials:
			#print "Skipping", jamcoin
			continue;
		print "Case #"+str(found), jamcoin,
		for nt in nonTrivials:
			print nt,
		print ""
		found+=1
		if found > J:
			return

def validateJamCoin(jamcoin):
	jamcoins = []
	for base in range(2, 11):
		baseNVal = int(jamcoin, base)
		nonTrivial = findNonTrivialDivisor(baseNVal)
		jamcoins.append(nonTrivial)
	return jamcoins


if __name__ == "__main__":

	print findJamCoin(16, 50)
	#validateJamCoin("1000000000000011")

