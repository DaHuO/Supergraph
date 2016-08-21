import sys

def primeCheck(n):
	# sieve holds all the numbers that still can be divisors
	upperBorder = int(n**0.5)+1
	sieve = [True]*upperBorder
	sieve[0] = False
	sieve[1] = False
	for i in xrange(upperBorder):
		# If we already know that the number is not a divisor, just skip it
		if (sieve[i] == False):
			continue
		# Return divisor
		if (n % i == 0):
			return i
		# Eliminate all multiples of the non-divisor
		else:
			for j in xrange(i, int(upperBorder / i), i):
				sieve[j] = False
	return None

if (len(sys.argv) < 2):
	print "Need inputfile as argument"
	exit(1)

#read file
input = list()
with open(sys.argv[1], 'r') as f:
	input = f.read().splitlines()
input.pop(0)

#convert to int list
input = map(lambda s: map(int, s.split(' ')), input)

def listToStr(indexList):
	indexListStr = ""
	for index in indexList:
		indexListStr += str(index)+" "
	indexListStr = indexListStr[:-1]
	return indexListStr

#compute
output = list()
for (N, J) in input:
	for i in xrange(int("1"+"0"*(N-2),2), int("1"*(N-1),2)+1):
		if (len(output) >= J):
			break
		bitString = bin(i)[2:]+"1"

		isPrime = False
		divisors = list()

		# Find Divisors or that one of the interpretations is prime
		for base in range(2,11):

			n = int(bitString,base)
			divisor = primeCheck(n)

			if (divisor is None):
				isPrime = True
				break
			else:
				divisors.append(divisor)
				print "n:  "+str(n)+"   d: "+str(divisor)
		# If none of the interpretations were prime, we found a jamcoin
		if (not isPrime):
			output.append(str(bitString)+" "+listToStr(divisors))

#write file
with open('output_coinjam.txt', 'w') as f:
	f.write("Case #1:\n")
	for line in output:
		f.write(line+"\n")
