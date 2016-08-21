from math import *

def coinJamBaseConvert(n):
	dividers = n + ' '
	#print "Turning other bases"
	for base in range(2, 11):
		#print 'Base', base
		newBase = 0
		for i in range(0, len(n)):
			#newBase += int(n[i]) * pow(base, (len(n)-1-i))
			newBase = newBase * base + int(n[i])
		p = checkNotPrime(newBase)
		if not p:
			dividers = n + ' '
			return False
		else:
			dividers += str(p) + ' '
	return dividers
	
def checkNotPrime(n):
	#print "Checking n for prime", n
	# if n == 0 or n == '1':
	# 	return False
	# elif n == 2:
	# 	return True
	# else:
	for i in xrange(2, 1000):
		#print i 
		if i*i > n:
			return False
		if n%i == 0:
			return i
	# the num IS prime
	return False

def convertDecToBin(n):
	res = []
	if n == 0:
		res.insert(0, '0')
	while n != 0:
		res.insert(0, str(n%2))
		n = int(n//2)
	return ''.join(res)

def generateNumbers(J, N):
	k = 0
	for i in xrange(0, int(pow(2, N-2))):
		d = convertDecToBin(i)
		a = '1' + '0'*(N-2-len(d)) + d + '1'
		m = coinJamBaseConvert(a)
		if m:
			print m
			k += 1
		if k == J:
			return

T = int(raw_input().strip())
for i in range(0, T):
	N, J = map(int, raw_input().strip().split(" "))
	print 'Case #' + str(i+1) + ':'
	generateNumbers(J, N)