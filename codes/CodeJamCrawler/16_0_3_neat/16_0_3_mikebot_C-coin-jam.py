import sys
from random import randrange

# Import the file as a list of lines:
size = sys.argv[1]

path = '/Users/mikevanderheyden/GitHub/codejam/2016/Qual/'
fin = path + 'C-' + size + '.in.txt'
fout = path + 'C-' + size + '.out.txt'

if size == 'large':
	n = 32
	j = 500
else:
	n = 16
	j = 50

def postponed_sieve():                 
	from itertools import count
	yield 2; yield 3; yield 5; yield 7;
	sieve = {}                         
	ps = postponed_sieve()             
	p = next(ps) and next(ps)          
	q = p*p                            
	for c in count(9,2):               
		if c in sieve:               
			s = sieve.pop(c)         
		elif c < q:  
			yield c                 
			continue              
		else:
			s=count(q+2*p,2*p)      
			p=next(ps)              
			q=p*p                   
		for m in s:                 
			if m not in sieve:      
				break
		sieve[m] = s   

def generate_primes(n):
	for p in postponed_sieve():
		if p > n:
			break
		yield p

def is_prime(n):
	ceil = (n ** 0.5) + 1
	isprime = 1
	for p in generate_primes(ceil):
		if n%p == 0:
			isprime = 0
	if n == 0 or n == 1:
		isprime = 0
	elif n == 2:
		isprime = 1
	return isprime

def generate_strings(l):
	l_inside = l-2
	maxl = 2**(l-1)
	for i in xrange(maxl):
		inside = bin(i)[2:]
		leading_zeros = l_inside - len(inside) + 1
		yield '1' + '0'*leading_zeros + inside + '1'

def check_base(s,b):
	'''
	Takes a string of 1s and 0s and returns the decimal 
	number represented by the string in the given base.
	
	l = len(s)
	tot = 0
	for d in s:
		l -= 1
		if d == '1':
			tot += b**l
	return tot
	'''
	digits = list(s)
	n = 0
	for d in digits:
		n = b * n + int(d)
	return n



small_primes = []
for i in xrange(1,1000):
	if is_prime(i):
		small_primes.append(i)



def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def find_divisor(n):
	for i in xrange(2,10000):
		if n%i == 0:
			return i
	return 1


def make_jamcoins(l,n):
	with open(fout,'wb') as f:		
		f.write('Case #1:\n')
		for c in generate_strings(l-1):
			#print 'GENERATED ' + c
			bases = []
			divisors = []
			stop = 0
			for i in xrange(2,11):
				cur = check_base(c,i)
				#print 'BASE %d: %d' % (i, cur)
				bases.append(cur)
				if probably_prime(cur,100):
					stop = 1
					break
				#print divisors
				divisors.append(find_divisor(cur))
			if stop == 1 or 1 in divisors:
				continue
			answer = c
			for d in divisors:
				answer += ' '
				answer += str(d)
			answer += '\n'
			f.write(answer)
			n -= 1
			if n == 0:
				break



make_jamcoins(n,j)






'''	
with open(fout,'wb') as f:
	for i in xrange(j):



	f.write('Case #' + str(i) + ': ' + str(cur_n) + '\n')
'''