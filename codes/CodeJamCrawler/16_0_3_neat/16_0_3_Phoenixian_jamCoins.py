def interpretBase(number, base):
	output = number % 10
	placeValue = 1
	while number > 0:
		number = number // 10
		output += (number % 10) * (base ** placeValue)
		placeValue += 1
	return output

def nextPrime(start, smallerPrimes):
	possibility = start
	while 1:
		isPrime = True 
		for prime in smallerPrimes:
			if possibility % prime == 0:
				isPrime = False 
				break
		if isPrime:
			return possibility
		possibility += 1 

def firstNPrimes(numPrimes):
	primes = [2]
	for index in range(numPrimes - 1):
		primes.append(nextPrime(primes[-1] + 1, primes))
	return primes

def extractDigitN(number, digitPlace):
	for cut in range(digitPlace):
		number = number // 10
	return number % 10
	
def nextCoin(coin, length):
	coin += 10 
	for place in range(1, length):
		digit = extractDigitN(coin, place) #((coin % (10 ** (place + 1))) - (coin % (10 ** place))) / (10 ** place)
#		print("digit", digit)
		if digit >= 2:
			coin -= digit * (10 ** place)
			coin += 10 ** (place + 1)
			
	return int(coin)
	
def findDivisor(number):
	for prime in primes:
		if number % prime == 0 and number != prime:
			#print(number, "divisible by", prime)
			return prime
	return -1

def isJamCoin(coin):
	divisors = []
	for base in range(2, 11):
		divisor = findDivisor(interpretBase(coin, base))
		if divisor == -1:
			return False
		divisors.append(divisor)
	return divisors

def answer(coin, divisors):
	print(coin, divisors[0], divisors[1], divisors[2], divisors[3], divisors[4], divisors[5], divisors[6], divisors[7], divisors[8])

initialCoin = 10000000000000000000000000000001
coin = initialCoin
	
primes = firstNPrimes(10000)
#print(primes)
print("Case #1:")

jamCoinsFound = 0
while jamCoinsFound < 500:
	divisors = isJamCoin(coin)
	if divisors != False:
		answer(coin, divisors) 
		jamCoinsFound += 1 
	coin = nextCoin(coin, 32)
# for i in range(2 ** 22):
	# if i % 2 ** 12 == 0:
		# print(i, coin)
	# coin = nextCoin(coin, 32)
