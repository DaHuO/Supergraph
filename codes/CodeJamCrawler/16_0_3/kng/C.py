from math import sqrt, ceil
def add(s):
	l = len(s)-1
	c = 1
	while(l>-1 and c==1):
		if(s[l]==1 and c==1):
			s[l] = 0
		elif(s[l]==0 and c==1):
			s[l] = 1
			c = 0
		l -= 1
	return s

def prime(a):
	if(a==2):
		return [True, 1]
	if(a%2==0):
		return [False, 2]
	b = int(sqrt(a))
	b += (b+1)%2
	while(b>2):
		if(a%b==0):
			return [False, b]
		b -= 2
	return [True, 1]

def not_prime(l):
	d = []
	for x in l:
		z = x[1]
		w = prime(z)
		if(w[0]==False):
			d.append(w[1])
	return d

def next(s, n, j):
	m = n-1
	l = [[i, 0] for i in xrange(2, 11)]
	while(m>-1):
		for i in xrange(9):
			l[i][1] += (l[i][0]**(n-1-m))*s[m]
		m -= 1
	d = not_prime(l)
	return [s, d]

input_file = open('C-large.in', 'r+')
output_file = open('C-large.out', 'w+')

t = int(input_file.readline())
c = 0

while(c<t):
	c += 1
	output_file.write('Case #'+str(c)+': \n')
	n,j = map(int, input_file.readline().strip().split(' '))
	s = [1] + [0 for _ in xrange(n-2)] + [1]
	#print s
	while(j>0):
		s, d = next(s, n, j)
		if(s[0]==1 and s[-1]==1 and len(d)==9):
			j -= 1
			print s, d
			z = ''
			for y in s:
				z += str(y)
			z += ' '
			for y in d:
				z += str(y)
				z += ' '
			output_file.write(str(z)+'\n')
		s = add(s)
