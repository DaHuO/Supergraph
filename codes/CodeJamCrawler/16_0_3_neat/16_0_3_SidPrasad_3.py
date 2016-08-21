from sys import stdin, stdout
from random import randint
from itertools import compress
from operator import mul

def radix(b) :
    while b :
        yield b & 1
        b >>= 1

def squares(b) :
    while True :
        yield b
        b *= b

def fast_exp(b, exp) :
    return reduce(mul, compress(squares(b), radix(exp)), 1)

def prime_sieve(limit):
	Prime = [True] * limit
	Prime[0] = Prime[1] = False

	for (i, isprime) in enumerate(Prime):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):
				Prime[n] = False


T = int(input())
mem = {}
Prime = list(prime_sieve(10000000))
#print type(Prime)
#Prime = next(P, None)
for t in xrange(T):
	N, J = [int(x) for x in stdin.readline().rstrip().split()]
	stdout.write( "Case #"+str(t+1) + ": " + "\n" )
	# print J
	# for j in Prime:
	# 	print j
	#print Prime[10]
	jj = 0
	while jj < J:
		#print jj
		while 1:
			ans = "1"
			for j in xrange(N-2):
				ans += str(randint(0,1))
			ans += "1"
			if ans in mem:
				continue
			else:
				#print ans
				mem[ans] = 1
				break
		lst = []
		for i in xrange(2, 11):
			#print i
			for j in xrange(150):
				num = 0
				md = Prime[j]
				#print j
				for k in xrange(N):
					#print k
					if ans[k]=='1':
						#print 1
						num += fast_exp(i, k)
						#print num
						num = num % md
				if num==0:
					#print 1
					lst.append(Prime[j])
					break
		if len(lst) == 9:
			ans = ans[::-1]
			stdout.write(ans + " ")
			for x in lst:
				stdout.write(str(x) + " ")
			stdout.write("\n")
			jj += 1
		
			