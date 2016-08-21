import math

def findDivisor(num):
	for i in range(2,int(math.sqrt(num))+5):
		if num % i == 0:
			return i
	return -1

def convertFromBase(num, base):
	result = 0
	i = 0
	while num > 0:
		result = result + (num%2) * (base**i)
		num = num // 2
		i = i + 1
	return result

def toBinary(num):
	return "{0:b}".format(num)

t = int(input())
for tc in range(t):
	n, wanted = [int(x) for x in input().split()]
	print("Case #{0}:".format(tc+1))
	found = 0
	for j in range(2**(n-2)):
		num = 2**(n-1)+2*j+1
		divisors = []
		valid = True
		for base in range(2,11):
			dec = convertFromBase(num,base)
			#print(base)
			#print(dec)
			d = findDivisor(dec)
			#print(d)
			if d != -1:
				divisors.append(d)
			else:
				valid = False
				break
		if valid:
			found = found + 1
			print(toBinary(num), end='')
			for d in divisors:
				print(" {0}".format(d),end = '')
			print()
		if found == wanted:
			break