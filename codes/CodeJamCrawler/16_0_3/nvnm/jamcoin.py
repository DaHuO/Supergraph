from math import sqrt


def miller_rabin(n, k=10):
	from random import randrange
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in xrange(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in xrange(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True


def binIncrement(bin):
	bin = [int(x) for x in bin]
	for x in range(len(bin)-1,-1,-1):
		if bin[x]!=1:
			bin[x] = 1
			break
		else:
			bin[x] = 0
	return ''.join([str(x) for x in bin])

def binToBase(bin,base):
	s = ''.join([str(x) for x in bin])
	return int(s,base)

T = input()
while T:
	N,J = (int(x) for x in raw_input().split())
	bin = '0'*(N-2)
	bin = '1'+bin+'1'
	print "Case #1:"
	while J:
		if bin == '1'*N: break
		div = []
		result = True
		for x in range(2,11):
			num = int(bin,x)
			result = result and not miller_rabin(num)
			if result == False:
				break
			for i in range(2,int(sqrt(num)+1)):
				if num%i==0 and num!=i:
					div.append(i)
					break

		if result:
			J-=1
			print bin," "," ".join([str(x) for x in div])

		bin = '1' + binIncrement(bin[1:-1]) + '1'
	T-=1