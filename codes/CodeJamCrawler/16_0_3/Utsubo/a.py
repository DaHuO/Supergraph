import random
import sets

def generate(n):
	n -= 2
	s = "1"
	for i in xrange(n):
		if random.randint(0,1) == 1:
			s += "1"
		else:
			s += "0"
	s += "1"
	return s

def isPrime(n):
	# ed = int(n**0.5)+1
	ed = 1000
	for i in xrange(2, ed):
		if n%i == 0:
			return i
	return -1

def check(s):
	l = []
	for i in range(2,11):
		n = int(s,i)
		res = isPrime(n)
		l.append(res)
		if res == -1:
			return (False,[])
	return (True,l)

t = raw_input()
(N,J) = map(int,raw_input().split())
st = sets.Set()

print "Case #1:"
while len(st) != J:
	s = generate(N)
	if s in st:continue
	(ok,lis) = check(s)
	if ok:
		print s,
		for i in lis:
			print i,
		print
		st.add(s)


