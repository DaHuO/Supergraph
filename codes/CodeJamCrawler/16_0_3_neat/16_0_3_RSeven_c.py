from math import sqrt

primeList = []
isPrime = []
def sieve(limit):
	isPrime = [True] * limit
	isPrime[0] = isPrime[1] = False

	for (i, isprime) in enumerate(isPrime):
		if isprime:
			primeList.append(i)
			if i*i <= limit:
				for n in xrange(i*i, limit, i):
					isPrime[n] = False

sieve(65539) # sqrt(2^32)

def base2(x):
	if x < 2:
		return str(x)
		
	return base2(x/2) + str(x%2)

def isPrimeF(x):
	if x < len(isPrime):
		return (isPrime[x], 0)
	
	for p in primeList:
		if p > sqrt(x):
			return (True, 0)
		
		if x % p == 0:
			return (False, p)
	
	return (True, 0)
	
c = input()
case = 1

while case <= c:
	n, j = str.split(raw_input())
	
	j = int(j)
	
	first, last = 0, 0
	
	first = 2**(int(n)-1) + 1
	last = 2**int(n)
	
	print "Case #"+str(case)+":"
	while first < last:
		num = first
		b2_num = base2(num)
		#print b2_num
		
		isJamCoin = True
		divisorList = []
		for i in xrange(2,11):
			#print i, b2_num, int(b2_num, base = i)
			convert = int(b2_num, base=i)
			res,divisor = isPrimeF(convert)
			if res:
				isJamCoin = False
				break
			else:
				divisorList.append(divisor)
		
		if isJamCoin:
			print b2_num + reduce(lambda x,y: str(x)+" "+str(y), divisorList, "")
			
			j -= 1
			if j == 0:
				break
		
		first += 2

	case += 1

