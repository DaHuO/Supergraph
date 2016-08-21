import math

N = 0
T = 0
J = 0
s = []
primes = []
powers = []
P = []

def gen_primes():
	global P, primes
	N = 10**16
	Nprimes = int(math.sqrt(N))+1
	primes = [ 0 for i in range(Nprimes)]
	len_primes = len(primes)
	sieve_lim = int(math.sqrt(len_primes))
	for i in range(2,sieve_lim+1):
		if primes[i] == 0:
			for j in range(i+i, len_primes, i):
				primes[j] = 1
	for i in range(2,len_primes):
		if primes[i] == 0:
			P.append(i)

def bk(k):
	global N, s, primes, powers, J
	
	if k == N-1:
		M = 9
		vals = []
		divs = [0 for i in range(M)]
		for b in range(2,11):
			val = 0
			for i in range(N):
				val += s[i]*powers[b-2][i]
			vals.append(val)

		vs = [0 for i in range(M)]
		for p in P:
			for i in range(M):
				if vs[i] == 0:
					if p < vals[i] and vals[i] % p == 0:
						divs[i] = p
						vs[i] = 1
		if sum(vs) == M and J > 0:
			J -= 1
			print ''.join(map(str, s)),' '.join(map(str,divs))
	else:
		for ii in [0,1]:
			s[k] = ii
			bk(k+1)

gen_primes()
T = int(raw_input())
for t in range(1,T+1):
	N, J = map(int, raw_input().strip().split(' '))
	s = [0 for i in range(N)]
	s[0] = s[len(s)-1] = 1
	for b in range(2, 11):
		powers.append([0 for i in range(N)])
		bb = 1
		for j in range(0, N):
			powers[b-2][N-j-1] = bb
			bb *= b
	print 'Case #%d:' % (t)
	bk(1)

#	print P