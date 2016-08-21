from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def pD(n):
	for i in islice(count(2), int(sqrt(n)-1)):
		if n%i == 0:
			return i

def interpret(jamcoin, base):
	s = 0
	for i in range(len(jamcoin)):
		if jamcoin[-(i+1)] == '1':
			s += base**i
	return s

N = 16
J = 50
so_far = 0
for a in xrange(2**(N-2)):
	myJ = "1" + ("{0:0" + str(N-2) + "b}").format(a) + "1"
	valid = True
	div = []
	for b in xrange(2, 11):
		n = interpret(myJ, b)
		if isPrime(n):
			valid = False
			break
		else:
			div.append(str(pD(n)))

	if valid:
		so_far += 1
		print myJ, ' '.join(div)
		if so_far == J:
			break