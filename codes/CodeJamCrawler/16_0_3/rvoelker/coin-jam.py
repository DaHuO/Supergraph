import gcjbase
from math import floor, sqrt
from sets import Set

primes = Set([2, 3])

def definitelyComposite(a, d, s, n):
	a = a % n

	if a == 0:
		return False

	if pow(a, d, n) == 1:
		return False

	for r in range(s):
		if pow(a, 2 ** r * d, n) == n - 1:
			return False

	return True

# Miller-Rabin Deterministic
def isPrime(n):
	if n in primes:
		return True

	if any((n % p) == 0 for p in primes):
		return False

	d = n - 1
	s = 0
	aSet = []

	while not d % 2 == 0:
		d = d >> 1
		s += 1

	# http://miller-rabin.appspot.com/
	if n < 341531:
		aSet = [9345883071009581737]
	elif n < 1050535501:
		aSet = [336781006125, 9639812373923155]
	elif n < 350269456337:
		aSet = [4230279247111683200, 14694767155120705706, 16641139526367750375]
	elif n < 55245642489451:
		aSet = [2, 141889084524735, 1199124725622454117, 11096072698276303650]
	elif n < 7999252175582851:
		aSet = [2, 4130806001517, 149795463772692060, 186635894390467037, 3967304179347715805]
	elif n < 585226005592931977:
		aSet = [2, 123635709730000, 9233062284813009, 43835965440333360, 761179012939631437, 1263739024124850375]
	else:
		aSet = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

	for a in aSet:
		if definitelyComposite(a, d, s, n):
			return False

	primes.add(n)
	return True

def findFirstDivisor(n):
	if n % 2 == 0:
		return 2

	for divisor in range(3, int(floor(sqrt(n))) + 1, 2):
		if isPrime(divisor) and n % divisor == 0:
			return divisor

	return n

def decimalTobinaryString(n, length):
	binaryString = bin(n)[2:]

	while len(binaryString) < length:
		binaryString = "0" + binaryString

	return binaryString

def generateCoinJams(inFile):
	output = "\n"
	n, j = map(int, inFile.readline().split())
	jamcoinsGenerated = 0
	innerBits = 0
	
	while innerBits < 2 ** (n - 2) and jamcoinsGenerated < j:
		binaryString = "1%s1" % (decimalTobinaryString(innerBits, n - 2))
		print("Trying: " + binaryString)
		coinjam = binaryString
		valid = True

		for base in range(2, 11):
			decimal = int(binaryString, base)

			if not isPrime(decimal):
				coinjam += " " + str(findFirstDivisor(decimal))
			else:
				valid = False
				break

		if valid:
			jamcoinsGenerated += 1
			output += coinjam

			if jamcoinsGenerated < j:
				output += "\n"

		innerBits += 1

	return output

gcjbase.run(generateCoinJams)