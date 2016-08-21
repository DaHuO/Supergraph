import math
import sys

primes = []

# Find all prime numbers for n-length binary
def isPrime(n):
	if n in primes:
		return True
	if (n <= 1):
		return False
	if (n == 2 or n == 3):
		primes.append(n)
		return True
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			return False
	primes.append(n)
	return True

def revertJamCoin(s, radix):
	n = 0
	for i in range(len(s)):
		n += int(s[-i-1])*pow(radix, i)
	return n

def isJamCoin(s):
	if (s[0] != '1' or s[-1] != '1'):
		return False
	for radix in range(2,11):
		if isPrime(revertJamCoin(s, radix)):
			return False
	return True

def nextJamCoin(s):
	if isJamCoin(s):
		s = bin(int(s,2)+1)[2:]
	while not isJamCoin(s):
		s = bin(int(s,2)+1)[2:]
	return s

def findFirstNTDivisor(n):
	if isPrime(n):
		return -1
	for i in range(2,n):
		if n % i == 0:
			return i
	return -1

outfile = open('answer.out', 'w')

with open(sys.argv[1], 'r') as f:
	inputs = [line.rstrip('\n') for line in f]

T = inputs[0]
[N, J] = [int(x) for x in inputs[1].split(' ')]

JamCoins = []
current = '1'+'0'*(N-1)
while len(JamCoins) < J:
	item = []
	current = nextJamCoin(current)
	item.append(current)
	for radix in range(2,11):
		item.append(str(findFirstNTDivisor(revertJamCoin(current, radix))))
	JamCoins.append(item)
	print(len(JamCoins),item)

outfile.write("Case #1:\n")
for item in JamCoins:
	outfile.write(' '.join(item))
	outfile.write('\n')

print('done')