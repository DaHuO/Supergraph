
def generateJamCoins(n, j, ub):
	startNumber = pow(2, n-1) + 1
	endNumber = pow(2, n)
	allNumbers = []
	currentNumber = startNumber
	currentCount = 0
	while currentNumber < endNumber and currentCount < j:
		isCurrentPrime = False
		for b in range(2, ub + 1):
			baseNumber = convertNumberToBaseB(bin(currentNumber)[2:], b)
			if isPrime(baseNumber):
				isCurrentPrime = True
				break
		if not isCurrentPrime:
			print currentNumber
			allNumbers.append(currentNumber)
			currentCount += 1
		currentNumber += 2
	return allNumbers

def generateFactors(jamCoins, ub):
	jamCoinsWithFactors = []
	for jamCoin in jamCoins:
		line = [bin(jamCoin)[2:]]
		for b in range(2, ub + 1):
			baseNumber = convertNumberToBaseB(bin(jamCoin)[2:], b)
			line.append(getFactor(baseNumber))
		jamCoinsWithFactors.append(line)
	return jamCoinsWithFactors



def convertNumberToBaseB (number, b):
	l = [int(digit) for digit in list(number)]
	numberBaseB = reduce(lambda x, y: x*b + y, l, 0)
	return numberBaseB

# Taken from http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def isPrime(n):
    """Returns True if n is prime."""
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n and i < 100:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

# Taken from http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def getFactor(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return n

def output(jamCoinsWithFactors):
	outputFile = open('output.txt', 'w')
	outputFile.write('Case #1:\n')
	for line in jamCoinsWithFactors:
		print line
		outputFile.write(line[0])
		i = 1
		while i < len(line):
			outputFile.write(' ' + str(line[i]))
			i += 1
		outputFile.write('\n')
	outputFile.close()

n = 32
j = 500
ub = 10

jamCoins = generateJamCoins(n, j, ub)
jamCoinsWithFactors = generateFactors(jamCoins, ub)
output(jamCoinsWithFactors)
