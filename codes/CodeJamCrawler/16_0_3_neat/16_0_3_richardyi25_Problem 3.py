from math import sqrt

def prime(n):
	i = 2
	while i < 1000:
		if n % i == 0:
			return i
		i += 1
	return False

def toBase(n, base):
	n = n[::-1]
	power = 0
	c = 0
	
	for ch in n:
		if ch == '1':
			c += pow(base, power)
		power += 1
	
	return c

count = 0
num = 0
big = pow(2, 30)

print "Case #1:"
while num < big:
	temp = str(bin(num)[2:])
	s = ''
	for i in range(30 - len(temp)):
		s += '0'

	n = '1' + s + temp + '1'
	d = []
	
	for j in range(2, 11):
		result = prime(toBase(n, j))
		d.append(result)
		if result == False:
			break
	else:
		count += 1
		print n, ' '.join([str(n) for n in d])
		if count >= 500:
			break
			
	num += 1