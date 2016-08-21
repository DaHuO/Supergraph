# I'm sure there's a more elegant solution, but with large probability this code will terminate 'quickly'. More precisely, the number of primes less than x is roughly x/ln(x). If one randomly chooses a number between 0,x it will be prime with probability ~ (x/ln(x))/x = 1/ln(x). Thus, the smaller the number, the larger the chance that it will be prime (btw, this neglects the fact that we have to output a number with a fixed number of digits so the chance will actually be even smaller since primes are sparser for larger numbers).

#The smallest number we will encounter will be in the small data set in base 2: 2^16. The chance that a randomly chosen number in this case is prime is then on the order of 1/16. As the base increases, the chance of it being prime decreases. As a result, the change that a number will be composite in all bases 2,3,4,...,10 is larger than (1-1/16)^9 ~ 55%. Thus, on average we will have to just look at ~2x the number of candidates as we need jamcoins (50 for the small data set). For the larger data set it's even better since then we're dealing with 32 digit numbers so the individual chance of it being composite increases to something larger than (1-1/32)^9 ~75%. Again, we won't have to look at too many numbers.

# So, in short my strategy is simply to randomly generate numbers with N digits that start and end with 1 and simply check to see if they're jamcoins and if so grab their smallest non-trivial divisor (which will also be small with large change since primes are denser at small numbers).



import random
N = 32
J = 1

def rand_num(length):
	r = [random.randint(0,1) for i in range(length - 2)]
	return [1] + r + [1]

def num_in_base(digits, base):
	num_digits = len(digits)
	return sum([digits[i] * base**(num_digits - 1 - i) for i in range(num_digits)])

def find_divisor(num):
	for i in range(2,int(num**0.5)):
		if num%i == 0:
			return i
	return -1

def generate_jamcoin(NSize):
	bases = [2,3,4,5,6,7,8,9,10]
	while True:
		guess = rand_num(NSize)
		divisors = [find_divisor(num_in_base(guess, b)) for b in bases]
		allGood = True
		for d in divisors:
			if d == -1:
				allGood = False
		if allGood:
			return ["".join([str(g) for g in guess])] + [str(div) for div in divisors]


fout = open('out.txt','w')
fout.write('Case #1:\n')
for i in range(J):
	fout.write(' '.join(generate_jamcoin(N)) + '\n')
fout.close()
