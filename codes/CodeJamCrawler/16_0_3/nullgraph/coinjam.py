#!/usr/bin/env python

import itertools

def firstFactor(n):
	if n < 2: 
		return -1;
	if n % 2 == 0:             
		return 2  # return False
	k = 3
	while k*k <= n:
		if n % k == 0:
			return k
		k += 2
	return -1

def firstFactorInAllBases(s):
	factors=[]
	for base in range(2, 11):
		n=int(s,base)
		k = firstFactor(n)
		if k != -1:
			factors.append(k)
		else:
			return -1
	return factors

def generateWallet(biglist, j):
	wallet={}
	for coin in biglist:
		s = ''.join(coin)
		if len(wallet) < j:
			factors = firstFactorInAllBases(s)
			if (factors != -1) and (not wallet.has_key(s)):
				wallet[s]=factors
		else:
			return wallet

def generatePotentialCoins(n):
	l=[]
	biglist = list(itertools.product(['0', '1'], repeat=n))
	for i in biglist:
		if i[0]=='1' and i[len(i)-1]=='1':
			l.append(''.join(i))
	return l


def main():
	l = readInput("small.in")
	print l
	n = int(l[0])
	j = int(l[1])
	fakeCoins = generatePotentialCoins(n)
	wallet = generateWallet(fakeCoins, j)
	# print wallet
	writeOutput(wallet, "small.out")

def readInput(filename):
	file = open(filename, "r")
 	file.readline()
 	line = file.readline()
 	file.close()
 	return line.split()

def writeOutput(output, filename):
	file = open(filename, "w")
	file.write("Case #1:\n")
	for key in output:
		file.write("%s" % key)
		for value in output[key]:
			file.write(" %s" % value)
		file.write("\n")
	file.close()

if __name__ == "__main__":
    main()