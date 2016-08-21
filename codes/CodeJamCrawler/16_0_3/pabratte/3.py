#!/usr/bin/python
import sys

def isPrime(n):
	i = 2
	while i<=100000:
		if n%i == 0:
			return False, i
		i = i + 1
	return True, 0

def strToBase(string, base):
	n = 0
	pos = len(string) - 1
	for i in range(0, len(string)):
		if string[pos] == '1':
			n = n + pow(base, i)		
		pos = pos -1 
	return n


def produceBaseCoin(size):
	return '1'+'0'*(size-2)+'1'


def nextCoin(c):
	coin = list(c)
	pos = len(coin) - 2
	carry = False;
	if coin[pos] == '0':
		coin[pos] = '1'
	else:
		coin[pos] = '0'
		carry = True
	while carry:
		carry = False;
		pos = pos - 1
		if coin[pos] == '0':
			coin[pos] = '1'
		else:
			coin[pos] = '0'
			carry = True
	return ''.join(coin)



def testCoin(coin):
	print "- Testing Coin: %s"%coin;
	divisors = []
	for base in range(2, 11):
		toNum = strToBase(coin, base)
		sys.stdout.write(" - Base (%i): %i -> "%(base, toNum))
		(res, divisor) = isPrime(toNum)		
		if res:
			print 'NOOOO! prime'
			return (False, divisors);
		else:
			print 'OK! (divisor: %i)'%divisor
			divisors.append(divisor)	
	return (True, divisors);



if __name__ == '__main__':
	input = open(sys.argv[1])
	output = open(sys.argv[1]+'.out', 'w')

	T = int(input.readline())
	for t in range(0, T):
		(coinLenght, nCoins) = [int(x) for x in input.readline().split()]
		output.write('Case #%i:\n'%int(t+1));
		coin = produceBaseCoin(coinLenght);
		
		for c in range(0, nCoins):
			print "FOUND %i COINS"%c
			(result, divisors) = testCoin(coin)
			while result == False:
				coin = nextCoin(coin)
				(result, divisors) = testCoin(coin)
			# print coin
			output.write("%s "%coin)

			# print divisors
			output.write(' '.join("%s"%i for i in divisors))
			output.write('\n')
			coin = nextCoin(coin)
	input.close()
	output.close()


