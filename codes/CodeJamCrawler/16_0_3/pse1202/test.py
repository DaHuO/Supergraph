filename = 'test.txt'
f = open(filename,'r')

def basek(n,k):
	a = 0
	n = str(n)
	for i in range(len(n)):
		a += (k**i)*int(n[-1-i])
	return a
def primesbelow(N):
	# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
	#""" Input N>=6, Returns a list of primes, 2 <= p < N """
	correction = N % 6 > 1
	N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
	sieve = [True] * (N // 3)
	sieve[0] = False
	for i in range(int(N ** .5) // 3 + 1):
		if sieve[i]:
			k = (3 * i + 1) | 1
			sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
			sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
	return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]
smallprimeset = list(set(primesbelow(70000)))
smallprimeset.sort()
_smallprimeset = 70000
def isprime(n, precision=7):
	if n < 1:
		raise ValueError("Out of bounds, first argument must be > 0")
	elif n <= 3:
		return n >= 2
	elif n % 2 == 0:
		return False
	elif n < _smallprimeset:
		return n in smallprimeset
	d = n - 1
	s = 0
	while d % 2 == 0:
		d //= 2
		s += 1
	for repeat in range(precision):
		a = random.randrange(2, n - 2)
		x = pow(a, d, n)

		if x == 1 or x == n - 1: continue

		for r in range(s - 1):
			x = pow(x, 2, n)
			if x == 1: return False
			if x == n - 1: break
		else: return False
	return True

T = int(f.readline())
for t in range(1,T+1):
	N,J = map(int,f.readline().split())
	print "Case #%d:" % t
	ans = 0
	for i in xrange(2**(N-2)):
		x = list()
		a = int(bin(2*i + 2**(N-1) + 1)[2:])
		b = True
		for j in range(2,11):
			n = basek(a,j)
			for k in smallprimeset:
				if n % k == 0:
					x.append(k)
					break
				elif k > n**0.5:
					b = False
					break
			if not b:
				break
		if b and len(x) == 9:
			print a,
			for k in x:
				print k,
			print
			ans += 1
		if ans >= J:
			break


