from math import sqrt
from itertools import count, islice
import argparse, random
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
inputFile = open(args.filename, 'r')
outputFile = open('output.txt', 'w')

numberOfCases = int(inputFile.readline().strip())

def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

for case in xrange(0,numberOfCases):
	outputFile.write('Case #1:\r\n')
	N, J = inputFile.readline().strip().split(' ')
	N = int(N)
	J = int(J)
	coinCoint = 0
	usedCoins = []
	while coinCoint < J:
		coin = ''.join(random.choice('01') for _ in range(N))
		coin = list(coin)
		coin[0] = '1'
		coin[N-1] = '1'
		coin = ''.join(coin)
		solveable = True
		base = 2

		divisorList = {
			2: 0,
			3: 0,
			4: 0,
			5: 0,
			6: 0,
			7: 0,
			8: 0,
			9: 0,
			10: 0
		}

		if coin not in usedCoins:
			while solveable and base <= 10:
				convertedCoin = int(coin, base)

				if isPrime(convertedCoin):
					solveable = False

				divisorFound = False
				divisor = 2
				while not divisorFound and solveable:
					remainder = convertedCoin % divisor
					if remainder == 0:
						divisorList[base] = str(divisor)
						divisorFound = True
					else:
						divisor += 1

					if divisor > (convertedCoin/2):
						solveable = False
				base += 1

			if solveable:
				outputFile.write('%s %s\r\n' %(coin, ' '.join(divisorList.values())))
				print '%s %s\r\n' %(coin, ' '.join(divisorList.values()))
				coinCoint += 1
				usedCoins += coin
