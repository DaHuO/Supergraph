# Code Jam 2016: Problem 3

import Primes

def compute_jamcoins(digits, n):
	
	b2_max = int("1"*digits,2)
	b2_min = int("1" + (digits-2)*"0" + "1", 2)
	
	primes = Primes.primes

	jamcoins = {}

	i = b2_min

	while len(jamcoins) < n:

		potential = bin(i)[2:]

		value = 0
		
		factors = [potential]

		for j in range(2, 11):
			value = 0
			value = Primes.isPrime(int(potential,j))
			if not value:
				break
			factors.append(str(value))

		if value:
			jamcoins[potential] = factors
			print(' '.join(factors))

		i += 2

	return jamcoins 

def validate_jamcoins(jamcoins):

	for i in jamcoins:
		for b in range(2, 11):
			if (int(i, b) % int(jamcoins[i][b - 1])):
				print ("ERROR: " + i + " does not have factor " + str(jamcoins[i][b-2]))
				print ("       Base: " + str(b) + ", Value: " + str(int(i,b)))

# Read line with the number of cases
t = int(input())
for i in range(1,t+1):
	n, m = [int(s) for s in input().split(" ")]
	print("Case #{}:".format(i))
	result = compute_jamcoins(n,m)