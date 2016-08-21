import math

def binary(num):
	s=""
	while num != 0:
		s = str(num%2) + s
		num = num/2
	return s

def isPrime(n):
	for x in range(2,int(math.sqrt(math.sqrt(math.sqrt(n))))):
		if n%x == 0:
			return x

	return 0

t = int (raw_input())
n, m = [int(s) for s in raw_input().split(" ")]
count = 0
print "Case #1:"
num1 = 2**(n-2)
num = binary(int(num1))
num += "1"

while (len(num) < n+1):
	array1 = [0]*9
	array = [0]*9
	for x in xrange(2, 11):
		sum = 0
		for y in xrange(0, n):
			sum = sum + (x**y)*int(num[len(num)-y-1])
		array[x-2] = sum

	for z in xrange(0, len(array)):
		array1[z] = isPrime(array[z])

	if 0 not in array1:
		print num, 
		for x in xrange(0, len(array1)):
			print array1[x],
		print 
		count += 1

	if count == m:
		break
	num1 += 1
	num = binary(int(num1))
	num += "1"
