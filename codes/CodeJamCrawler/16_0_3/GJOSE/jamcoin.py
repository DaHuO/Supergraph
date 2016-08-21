import sys
from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True

INPUT = "C-small-attempt0.in.txt"
OUTPUT = "C-small-attempt0.out.txt"

def my_print(text):
    sys.stdout.write(str(str(text)) + "\n")
    sys.stdout.flush()

def readFile(filename):
	with open(filename) as f: 
		return [x.strip('\n') for x in f.readlines()]

def writeLine(output, line):
	with open (output, 'a') as f: 
		f.write(line + "\n")

def isPrimeOrDivisor(n):
	# my_print("checking " + str(n))
	if n == 0 or n == 1: 
		return False
	for i in range(2, n): 
		if n%i == 0:
			return i
	return True


def getFirstDivisor(n):
	for i in range(2, n): 
		if n%i == 0:
			return i

# def isPrime(n):
# 	if n == 0 or n == 1: 
# 		return False
# 	for i in range(2, n): 
# 		if n%i == 0:
# 			return False
# 	return True


def checkAllBases(n): 
	divisors = []
	ints = []
	for i in range(2, 10 + 1):
		my_print("Checking " + str(n) + "in base " + str(i) + ": " + str(int(str(n), i)))
		temp = isPrime(int(n, i))
		ints = ints + [int(n, i)]
		if temp == True:
			return False
		else:
			divisors = divisors + [temp]
	return True

def getDivisors(n): 
	divisors = []
	ints = []
	for i in range(2, 10 + 1):
		# my_print("finding divisors for  " + str(int(str(n), i)))
		temp = getFirstDivisor(int(n, i))
		divisors = divisors + [temp]
			# my_print("Divisors for " + str(n) + " " + str(divisors))
	return divisors

def getPermutations(length):
	length = length - 2
	jamcoins = []
	highestInt = int("1" * length, 2)
	for i in range(0, highestInt + 1):
		_str ="1" +  ("{0:0" + str(length)+ "b}").format(i) + "1"
		jamcoins = jamcoins + [_str]
		# my_print("Found coin: " + _str)
	return (jamcoins)

def getJamCoins(permutations, numberRequired):
	jamCoins = []
	for i in range(0, len(permutations)):
		# my_print("Checking coin: " + str(len(jamCoins)) + " " + permutations[i])
		if isJamCoin(permutations[i]):
			my_print("Found coin: " + str(len(jamCoins)) + " " + permutations[i])
			jamCoins = jamCoins + [permutations[i]]
			if len(jamCoins) >=numberRequired:
				return jamCoins

def isJamCoin(_str):
	return checkAllBases(_str)

if __name__ == "__main__":
	print(isPrime(470184985873))
	content = readFile(INPUT)
	for i in range(1, len(content)):
		writeLine(OUTPUT, "Case #" + str(i) +":")
		line = content[i]
		[numDigits, numCoinsTarget] = line.split(' ')
		permutations = getPermutations(int(numDigits))
		my_print("Found " + str(len(permutations)) + " permutations")
		jamCoins = getJamCoins(permutations, int(numCoinsTarget))
		
		for jamCoin in jamCoins: 
			divisors = getDivisors(str(jamCoin))
			divisorString = ""
			for s in range(0, len(divisors)):
				divisorString = divisorString + str(divisors[s] )+ " "

			# print(jamCoin + " " + str(divisorString))
			writeLine(OUTPUT, jamCoin + " " + str(divisorString))

