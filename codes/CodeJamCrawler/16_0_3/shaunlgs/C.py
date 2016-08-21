def isPrime(num):
	if num <= 1:
		return False;
	elif num <= 3:
		return True;
	elif num % 2 == 0 or num % 3 == 0:
		return False;
	i = 5
	while i*i <= num:
		if num % i == 0 or num % (i+2) == 0:
			return False;
		i += 6
	return True;

def numberToCode(num, size):
	partialCode = bin(num)[2:]

	code = "0"*(size-1)
	code = "1" + code[1:]
	code = code[:-len(partialCode)] + partialCode
	code = code + "1"


	return code

def numInBase(numStr, base):
	total = 0
	for i in range(len(numStr)):
		total += int(numStr[i:i+1]) * pow(base, len(numStr)-1-i)
	return total

def jamCoin(numStr):
	for i in range(2,11):
		if(isPrime(numInBase(numStr,i))):
			return False
	return True

def nonTrivialDivisors(numStr):
	for i in range(2,11):
		number = numInBase(numStr,i)
		for j in range(2,number):
			if number % j == 0:
				print(j, end=" ")
				break

#T = input()

#for i in range(int(T)):
#	N, J = input().split()

print()

count = 0
success = 0

print ("Case #1:")
while success < 50:
	if(jamCoin(numberToCode(count,16))):
		print(numberToCode(count,16), end=" ")
		# show non trivial divisors
		nonTrivialDivisors(numberToCode(count,16))
		print()
		success += 1
	count += 1
