import itertools
import math

print "Case #1:"
N = 16 # length of jamcoins
J = 50 # number of jamcoins

def interpret(x,b):
	x = list(reversed(x))
	return sum([x[i]*(b**i) for i in range(len(x))])

def isPrime(n):
	for i in range(2,int(math.ceil(math.sqrt(n)))):
		if n%i == 0:
			return False
	return True

def smallDivisor(n):
	d = 0	
	i = 2
	while d == 0:
		if n%i == 0:
			d = i
		elif i > 100000:
			d = 1
		i += 1
	return d


numberOfCoins = 0
n = 0 
while True:
	j = [int(i) for i in list("{0:b}".format(2**(N-1) + 2*n + 1))]
	interpretations = [interpret(j,b) for b in range(2,11)]
	n += 1	
	listofDivisors = [smallDivisor(i) for i in interpretations]
	if all(j != 1 for j in listofDivisors):
		print "".join([str(x) for x in j]), " ".join([str(x) for x in listofDivisors])
		n += 1	
		numberOfCoins += 1
	if numberOfCoins == J:
		break


		
	
