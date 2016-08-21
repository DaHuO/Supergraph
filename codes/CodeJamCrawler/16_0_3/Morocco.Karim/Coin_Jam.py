#! /usr/bin/env python2.7

T=int(raw_input())
NJ=raw_input().split()
N=int(NJ[0])
J=int(NJ[1])

DivMax=212 # the max div to check
PrimeList=range(2,DivMax)

# for optimization, we build a list of primes less then DivMax
for i in range(4,DivMax):
	if i %2==0 :
		PrimeList.pop(PrimeList.index(i))
		continue
	j=3
	while j<=i**0.5:		
		if i %j==0 :
			PrimeList.pop(PrimeList.index(i))
			break
		j+=2
for test in range(1,T+1):
	# Approach : we will brute force the problem, start from the minimum number statisfying conditions on coinjam, and test whether it is a coinjam
	# or not, then move forward (by adding 2)
	CJlist=[]
	Nbr=2**(N-1)+1
	while len(CJlist)<J:
		#Nbr=eval("0b"+bin(i)[2:]+"1")
		IsJamCoin=True
		DivList=[]
		bits=[int(bit) for bit in list(bin(Nbr)[2:])]
		for base in range(2,11):
			# Calculat sting interpretation in base "base"
			M=0
			for j in range(len(bits)):
				M=M+bits[j]*base**j
			# Check primality, we will only check against primes in PrimeList, that's to say divisor less or equal to DivMax
			IsPrime=True
			RM=M**0.5
			j=0
			while j< len(PrimeList) & PrimeList[j] <=RM:
				prime =PrimeList[j]
				if M % prime==0:
					IsPrime=False
					DivList.append(prime)
					break
				j+=1
			if IsPrime:
				IsJamCoin=False
				break
		if IsJamCoin :
			CJlist.append([Nbr, DivList])
		Nbr+=2

	# We suppose that hopefully we have got J jamCoins of length N with divisors of their repesentations in base 2 to 10
	# we print the result
	
	print "Case #{}:".format(test)
	for line in CJlist:
		Nbr=line[0]
		bits=[str(bit) for bit in list(bin(Nbr)[2:])]
		bits.reverse()
		DivList=[str(prime) for prime in line[1]]
		print "".join(bits)+" "+ " ".join(DivList)


	#checking
	for line in CJlist:
		Nbr=line[0]
		DivList=line[1]
		bits=[int(bit) for bit in list(bin(Nbr)[2:])]
		for base in range(2,11):
			M=0
			for j in range(len(bits)):
				M=M+bits[j]*base**j
			if M % DivList[base-2] >0:
				print "you missed nbr=" , bin(Nbr)[2:] , "base= ", base
				