import numpy as np
import sys
from decimal import Decimal
import mpmath
def JamCoins(N,J,case):

	def div(n): # return -1 if non-trivial does not exist
		if n==2:
			return [ ]
		else:	
			for i in np.arange(2,1000,1):
				if (n % int(i)) == 0:
					return [int(i)]
			return [ ]

	def isJamCoin(jamCoin):
		divisors = []
		for d in np.arange(2,11,1):
			#print "###", "Base", d,
			val = int(jamCoin,d)
			#print val 
			L = div(val)
			#print L
			divisors  = divisors + L
		return divisors


	counter = 0
	print "Case #" + str(i+1) + ":"

	for j in np.arange(0,pow(2,N-2),1):
		sys.stderr.write(str(j) + "\n")
		# conver to binary
		strnum = str(bin(j))[2:]
		j2 = "1" + str("0"*(N-2-len(strnum))) + strnum + "1"
		#print j2


		divisor = isJamCoin(j2)
		if len(divisor)==9:
			print j2, 
			for e in divisor:
				print e,
			print 
			counter +=1
			if counter==J:
				return []




T = raw_input('')
for i in np.arange(0,int(T),1):
	NJ = raw_input('')
	N = int(NJ.split(" ")[0])
	J = int(NJ.split(" ")[1])
	JamCoins(N,J,i)
