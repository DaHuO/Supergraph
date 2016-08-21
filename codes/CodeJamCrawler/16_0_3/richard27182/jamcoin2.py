from math import sqrt

def isprime(n):
	if n<4:
		return 0
	elif n % 2==0:
		return 2
	else:
		testdivisor=3
		while testdivisor<=sqrt(n) and testdivisor<=10000: #much faster, but not all valid jamcoins will be found
			if n % testdivisor==0:
				return testdivisor
			testdivisor+=2
		return 0
	
def nobaseprime(coin):
	divisors=[0,0,0,0,0,0,0,0,0]
	binarycoin=bin(coin)[+2:]
	divisors[0]=isprime(coin)
	for coinbase in range(3,11):
		coinbaseinterpretation=int(binarycoin,coinbase)
		divisors[coinbase-2]=isprime(coinbaseinterpretation)
		if divisors[coinbase-2]==0:
			return divisors
	return divisors
	
t = int(input()) 
print("Case #{}:".format(t))
for i in range(1, t + 1):
	N,J=[int (s) for s in input().split(" ")]
	numcoins=0
	testcoin=2**(N-1)+1
	while numcoins<J:
		divisors=nobaseprime(testcoin)
		if not (0 in divisors):
			print("{} {} {} {} {} {} {} {} {} {}".format(bin(testcoin)[+2:],divisors[0],divisors[1],divisors[2],divisors[3],divisors[4],divisors[5],divisors[6],divisors[7],divisors[8]))
			numcoins+=1
		testcoin+=2
		
	
