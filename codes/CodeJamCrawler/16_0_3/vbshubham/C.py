primes = open('10000.txt').read().split()
def fact(num):
	for  p in primes:
		p = int(p)
		if num % p == 0:
			return p
		elif p*p>num:
			return None

n = 32
j = 500
N = 2**(n-1)+1
cnt=0
print 'Case #1:'
while cnt<j :
	s = '{0:b}'.format(N)
	N+=2
	evidence = []
	for i in range(10,1,-1):
		factor = fact(int(s,i))
		if factor == None:
			# print "prime",int(s,i)
			continue
		else:
			# print i,int(s,i),factor
			evidence.append(factor)
	if len(evidence)==9:
		cnt+=1
		evidence.reverse()
		print s,
		for f in evidence:
			print f,
		print	

