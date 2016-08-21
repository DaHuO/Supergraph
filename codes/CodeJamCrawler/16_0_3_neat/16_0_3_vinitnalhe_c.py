# def primes2(n):
#     """ Input n>=6, Returns a list of primes, 2 <= p < n """
#     n, correction = n-n%6+6, 2-(n%6>1)
#     sieve = [True] * (n/3)
#     for i in xrange(1,int(n**0.5)/3+1):
#       if sieve[i]:
#         k=3*i+1|1
#         sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
#         sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
#     return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
# primes = primes2(65600)
from math import sqrt
m1 = 32769
m2 = 65536
cnt = 50
print 'Case #1:'
def isValid(num,base):
	n = int(num,base)
	for i in range(2, int(sqrt(n))+1):
		if n%i == 0 :
			return i
	return False
ans = []
for i in range(m1,m2):
	num = bin(i)[2:]
	if num[-1] == '0':
		continue
	baseAns = []
	for base in range(2,11):
		tmp = isValid(num, base)
		if not tmp:
			break
		baseAns.append(tmp)
	if len(baseAns) == 9 :
		print num,
		for i in baseAns:
			print i,
		print ''
	if len(ans) >= cnt:
		break





