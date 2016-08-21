import sys
import random

N = 32 #int(sSample.split(' ')[0])
J = 500 #int(sSample.split(' ')[1])

binStrStart = '1' + ''.join(['0'] * (N-2)) + '1'
binStrEnd = ''.join(['1'] * N)

numMax = int(binStrEnd, 2)
numMin = int(binStrStart, 2)
#print numMax, numMin
#lstDivisors = []
#bNotPrimeFlag = False
#ranNum = 0
iTotalIterations = 0
lstSelectedNumbers = []
lstSelectedDivisors = []

while len(lstSelectedNumbers) < J and iTotalIterations < 100000:

	iTotalIterations = iTotalIterations + 1
	bNotPrimeFlag = False
	ranNum = 0
	lstDivisors = []
	while bNotPrimeFlag == False:

		ranNum = random.randint(numMin, numMax)

		while (ranNum % 2) == 0 or (ranNum in lstSelectedNumbers):
			ranNum = random.randint(numMin, numMax)

		#print ranNum, bin(ranNum)[2:]

		lstDivisors = []
		for base in range(2, 11):
			BaseT = int(bin(ranNum)[2:], base)
			#print BaseT, base
			bNotPrimeFlag = False
			iDivisor = 0

			if(BaseT < 25):
				# Do sequential Prime checking
				for i in range(2, BaseT):
					if (BaseT % i) == 0:
						bNotPrimeFlag = True
						iDivisor = i
						break

			else:
				#Do sequential Prime checking
				for i in range(2, 26):
					if (BaseT % i) == 0:
						bNotPrimeFlag = True
						iDivisor = i
						break

				#Do random prime checking
				if bNotPrimeFlag == False:
					for b in range(1000):
						randDivsor = random.randint(26, (BaseT-1))
					if (BaseT % randDivsor) == 0:
						bNotPrimeFlag = True
						iDivisor = randDivsor
						break

			if bNotPrimeFlag == False:
					break

			#print iDivisor
			lstDivisors.append(str(iDivisor))


	lstSelectedNumbers.append(ranNum)
	lstSelectedDivisors.append(lstDivisors)


lstBinSelectedNumbers = map(lambda x: bin(x)[2:], lstSelectedNumbers)

#print lstSelectedNumbers
#print lstBinSelectedNumbers
#print iTotalIterations
print "Case #1: "
for n in range(J):

	print "%s %s " % (lstBinSelectedNumbers[n], ' '.join(lstSelectedDivisors[n]))



