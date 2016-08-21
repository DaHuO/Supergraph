from math import sqrt

def checkPrime(n):
	for i in range(3, 1000):
		if(n % i == 0):
			return False

	return True

def findDivisor(n):
	i = 2

	while(True):
		if(n % i == 0):
			return i
		i = i + 1;

def convert(n, N, base):
	num = 0
	i = 0
	b = bin(n)[2:]

	while(i < N):
		if(int(b[i]) == 1):
			#print base, N-i-1
			num = num + base**(N-i-1)
		i = i + 1

	return num

T = raw_input()
tmp = raw_input()
N = int((tmp.split())[0])
J = int((tmp.split())[1])

n = 2**(N-1) - 1

print "Case #1:"

while(J > 0):
	n = n + 2

	num2 = convert(n, N, 2)
	num3 = convert(n, N, 3)
	num4 = convert(n, N, 4)
	num5 = convert(n, N, 5)
	num6 = convert(n, N, 6)
	num7 = convert(n, N, 7)
	num8 = convert(n, N, 8)
	num9 = convert(n, N, 9)
	num10 = convert(n, N, 10)

	if(checkPrime(num2) == True):
		continue
	else:
		d2 = findDivisor(num2)

	if(checkPrime(num3) == True):
		continue
	else:
		d3 = findDivisor(num3)

	if(checkPrime(num4) == True):
		continue
	else:
		d4 = findDivisor(num4)

	if(checkPrime(num5) == True):
		continue
	else:
		d5 = findDivisor(num5)

	if(checkPrime(num6) == True):
		continue
	else:
		d6 = findDivisor(num6)

	if(checkPrime(num7) == True):
		continue
	else:
		d7 = findDivisor(num7)

	if(checkPrime(num8) == True):
		continue
	else:
		d8 = findDivisor(num8)

	if(checkPrime(num9) == True):
		continue
	else:
		d9 = findDivisor(num9)

	if(checkPrime(num10) == True):
		continue
	else:
		d10 = findDivisor(num10)

	print num10, d2, d3, d4, d5, d6, d7, d8, d9, d10

	J = J-1