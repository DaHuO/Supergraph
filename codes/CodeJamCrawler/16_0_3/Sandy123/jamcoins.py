import sys
import math

def is_prime(num):
	if num == 2 or num == 3:
		return (True,num)
	if num % 2 == 0:
		return (False,2)
	i = 3
	limit = math.sqrt(num)
	# Just check till some range to make the program run faster
	# this will result in some numbers being declared prime even though they are not
	# So a valid jamcoin may get ignored due to this
	# As we just need any 500 jamcoins which satisfy all the conditions it should be fine
	while i <= limit and i <= 100000:
		if num % i == 0:
			return (False,i)
		i += 2
	return (True,num)

def convertToBase(num,base):
	numLength = len(num)
	number = num[::-1]
	result = 0
	for index in range(0,numLength):
		result = result + int(number[index]) * (base ** index)
	
	return result

def binaryValue(n,x):
	return bin(x)[2:].rjust(n, '0')

def solve(lines,index):
	line = lines[index].strip().split(' ')
	N , J = line[:]
	jamCoinFound = 0
	endRange = 2 ** (int(N)-2)
	numOfDigits = int(N) - 2
	num = 0
	while num < endRange:
		isJamCoin = True
		number = '1' + binaryValue(numOfDigits,num) + '1'
		divisors = []
		for base in range(2,11):
			baseXNumber = convertToBase(number,base)
			isPrime , divisor = is_prime(baseXNumber)
			if isPrime == False:
				divisors.append(str(divisor))
			else:
				isJamCoin = False
				break
		if isJamCoin == True:
			jamCoinFound += 1
			divisorsString = ' '.join(divisors)		
			print (str(number) + ' ' + divisorsString)
		if jamCoinFound >= int(J):
			break
		num += 1

def main():
	lines = sys.stdin.read().splitlines()
	numberOfTests = int(lines[0])
	for index in xrange(1,numberOfTests+1):
		print ('Case #' + str(index) + ':')
		solve(lines,index)

if __name__ == '__main__':
	main()