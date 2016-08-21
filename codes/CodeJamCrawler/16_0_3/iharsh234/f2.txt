import random
from math import sqrt
def primeListSofE(n) :
    maxI = (n-3) // 2
    maxP = int(sqrt(n))
    sieve = [True for j in xrange(maxI+1)]
    for p in xrange(3,maxP+1,2) :
        i = (p-3) // 2
        if sieve[i] :
            i2 = (p*p-3) // 2
            for k in xrange(i2,maxI+1,p) :
                sieve[k] = False
    ret = [2]+[2*j+3 for j in xrange(len(sieve)) if sieve[j]]
    return ret
 
seive = primeListSofE(10000000)
#print len(seive)
T = input()
N,M = map(int,raw_input().split())

_mrpt_num_trials = 10
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite
#print is_probable_prime(27)

har = dict()
num = 2 ** 16
for i in xrange(2,num+1):
	astr = bin(i)[2:]
	if astr[0] == astr[-1] == '1':
			if len(astr) not in har:har[len(astr)] = [astr]
			else:har[len(astr)].append(astr)
#print har
#ans = 0
#for i in har:
	#ans += len(har[i])
	#print i,len(har[i])
#print ans
#print har
#print int(har[5][1],9)
#print har[5][1]
a = 0
res = dict()
for y in har[N]:
		cnt = 0
		for j in xrange(2,11):
			if is_probable_prime(int(y,j)) == False:cnt += 1
		if cnt == 9:
			#print 	y
			res[y] = []
			for j in xrange(2,11):res[y].append((j,int(y,j)))
			a += 1
		if a == 51:break

data = dict()
"""
for k in  res:
	#print k,'-->',res[k]
	data[k] = dict()
	for x in sorted(res[k]):
		for y in seive:
			if x[1] % y == 0:
				#print x,max(x/y,y)
				data[k][x] = (x[1]/y,y)
				break
#print data
print res
for x in data:
	print x,
	for y in data[x]:
		print data[x][y],
	print
	
"""
I = M
print 'Case #1:'
for y in res:
	M -= 1
	print y,
	for j in res[y]:
		y2 = j[1]
		for y1 in seive:
			if y2 % y1 == 0:
				print max(y2/y1,y1),
				break
	print
	if M == 0:break
