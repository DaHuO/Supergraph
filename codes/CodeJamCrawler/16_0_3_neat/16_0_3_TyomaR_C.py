trivial_limit = 50
p = [0 for i in range(1000)]
from math import sqrt, floor, log
def gcd(a, b):
	while b:
		a %= b
		a, b = b, a
	return a

def powmod(a, b, m):
	res = 1
	while b:
		if b & 1:
			res = (res * a) % m
			b -= 1
		else:
			a = (a * a) % m
			b >>= 1
	return res

def miller_rabin(n):
	b = 2
	while gcd(n, b) != 1:
		g = gcd(n, b)
		if n > g:
			return False
		b += 1
	p = 0
	q = n - 1
	while (q & 1) == 0:
		p += 1
		q >>= 1

	rem = powmod (b, q, n)
	if rem == 1 or rem == n - 1:
		return True
	for i in range(1, p):
		rem = (rem * rem) % n
		if (rem == n - 1):
			return True
	return False

def jacobi(a, b):
	if a == 0: return 0
	if a == 1: return 1
	if a < 0:
		if (b & 2) == 0:
			return jacobi(-a, b)
		else:
			return -jacobi(-a, b)
	a1 = a
	e = 0
	while (a1 & 1) == 0:
		a1 >>= 1
		e += 1

	s = 228
	if (e & 1) == 0 or (b & 7) == 1 or (b & 7) == 7:
		s = 1
	else:
		s = -1
	if (b & 3) == 3 and (a1 & 3) == 3:
		s = -s
	if a1 == 1:
		return s
	return s * jacobi(b % a1, a1)

def bpsw(n):
	if int(sqrt(n)) * int(sqrt(n)) == n:
		return False
	dd = 5

	while True:
		g = gcd(n, abs(dd))
		if 1 < g and g < n:
			return False
		if jacobi(dd, n) == -1:
			break
		if dd < 0:
			dd = 2 - dd 
		else:
			dd = -2-dd
	p = 1
	q = (p * p - dd) // 4
	d = n + 1
	s = 0
	while (d & 1) == 0:
		s += 1
		d >>= 1
	u = 1
	v = p
	u2m = 1
	v2m = p
	qm = q
	qm2 = q + q
	qkd = q

	mask = 2
	while mask <= d:
		u2m = (u2m * v2m) % n
		v2m = (v2m * v2m) % n
		while v2m < qm2:
			v2m += n
		v2m -= qm2
		qm = (qm * qm) % n
		qm2 = qm * 2
		if d & mask:
			t1 = (u2m * v) % n
			t2 = (v2m * u) % n	
			t3 = (v2m * v) % n
			t4 = (((u2m * u) % n) * dd) % n
			u = t1 + t2
			if u & 1:
				u += n
			u = (u >> 1) % n
			v = t3 + t4
			if (v & 1):
				v += n
			v = (v >> 1) % n
			qkd = (qkd * qm) % n
		mask <<= 1

	if u == 0 or v == 0:
		return True
	qkd2 = qkd + qkd

	for r in range(1, s):
		v = (v * v) % n - qkd2
		if (v < 0):
			v += n
		if (v < 0):
			v += n
		if (v >= n):
			v -= n
		if (v >= n):
			v -= n
		if (v == 0):
			return True
		if (r < s-1):
			qkd = (qkd * qkd) % n
			qkd2 = qkd * 2
	return False

def prime (n):
	for i in range(trivial_limit):
		if p[i] >= n:
			break
		if (n % p[i] == 0):
			return False
	if (p[trivial_limit - 1] * p[trivial_limit - 1] >= n):
		return True
	if (not miller_rabin(n)):
		return False
	return bpsw(n)

def prime_init(): 
	i = 2
	j = 0
	while j < trivial_limit:
		pr= True
		k = 2
		while (k * k <= i):
			if (i % k == 0):
				pr = False			
			k += 1
		if (pr):
			p[j] = i
			j += 1 
		i += 1

prime_init()

def pollard_p1(n):
	b = 13
	q = [2, 3, 5, 7, 11, 13]
	a = 5 % n
	for j in range(10):
		while gcd(a, n) != 1:
			a = (a * a) % n
			a += 3
			a %= n

		for i in range(6):
			qq = q[i]
			e = floor(log(b) / log(qq))
			aa = powmod (a, powmod (qq, e, n), n)
			if (aa == 0):
				continue
			g = gcd (aa-1, n)
			if (1 < g and g < n):
				return g
	return 1

from random import randint
def pollard_rho(n, iterations_count = 100000):
	b0 = randint(0, n - 1)
	b1 = b0
	b1 = ((b1 * b1) % n + 1) % n
	g = gcd (abs (b1 - b0), n)
	for count in range(iterations_count):
		if g != 1 and g != n:
			break
		b0 = ((b0 * b0) % n + 1) % n
		b1 = (b1 * b1) % n + 1
		b1 = ((b1 * b1) % n + 1) % n
		g = gcd (abs (b1 - b0), n)
	return g

def pollard_monte_carlo(n, m = 100):
	b = randint(2, 100)

	primes = list()
	m_max = 0
	if len(primes) == 0:
		primes.append(3)
	if (m_max < m):
		m_max = m
		for prime in range(5, m + 1, 2):
			is_prime = True
			for j in primes:
				div = j
				if (div*div > prime):
					break
				if (prime % div == 0):
					is_prime = False
					break
			if (is_prime):
				primes.append(prime)
	g = 1
	for i in range(len(primes)):
		if g != 1:
			break
		cur = primes[i]
		while (cur <= n):
			cur *= primes[i]
		cur //= primes[i]
		b = powmod (b, cur, n)
		g = gcd (abs(b-1), n)
		if (g == n):
			g = 1
	return g

def supertrivial(n):
	if n & 1:
		return 1
	return 2

def trivial(n):
	i = 3
	while i * i <= min(n, 10**8):
		if n % i == 0:
			return i
		i += 2
	return 1

def pollard_bent(n, iterations_count = 19):
	b0 = randint(0, n - 1)
	b1 = (b0 * b0 + 2) % n
	a = b1
	series_len = 1
	for iteration in range(iterations_count):
		g = gcd (b1-b0, n)
		for ln in range(series_len):
			if g != 1 and g != n:
				break
			b1 = (b1*b1 + 2) % n
			g = gcd (abs(b1-b0), n)
		b0 = a
		a = b1
		if (g != 1 and g != n):
			return g		
		series_len *= 2
	return 1


def get_min_divisor(n):
	if prime(n):
		return n
	else:
		if supertrivial(n) != 1:
			return 2
		x = trivial(n) 
		if x != 1:
			return x
		a, b, c, d = pollard_monte_carlo(n), pollard_rho(n), pollard_p1(n), pollard_bent(n)
		if a == 1:
			a = n
		if b == 1:
			b = n
		if c == 1:
			c = n
		if d == 1:
			d = n
		return min(a, b, c, d)

def mindiv(s, base):
	n = 0
	for i in range(len(s)):
		n += s[i] * base ** (len(s) - 1 - i)
	m = get_min_divisor(n)
	if m == n: return -1
	return m

t = int(input())
n, need = map(int, input().split())

print("Case #1:")
printed = 0
for i in range(2 ** (n - 2)):
	s = [0] * n
	s[0] = s[n - 1] = 1
	for j in range(1, n - 1):
		if i & (1 << (j - 1)):
			s[j] = 1
	ok = True
	ans = [-1 for i in range(2, 11)]
	for j in range(2, 11):
		ans[j - 2] = mindiv(s, j)
		if ans[j - 2] == -1:
			ok = False
			break
	if ok:
		useless = 0
		print(''.join(map(str, s)), ' '.join(map(str, ans)))
		printed += 1
		if printed == need:
			break