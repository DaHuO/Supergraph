import itertools
import math
def baseConversion(n,l):
	y = len(str(n))
	x = [int(i) for i in str(n)]
	x.reverse()
	m = 0
	for i in range(0,y):
		p = x[i] * pow(l,i)
		m = m+p
	return m
#for i in range(2,11):
#	print(baseConversion(1101,i))

def divisor(n):
	for i in range(2,int(math.sqrt(n))):
		if (n % i == 0):
			return i
	
	return -1
def not_prime(n):
	if divisor(n) != -1: # prime 
		return True
	else:
		return False
#for i in range(2,11):
#	print((baseConversion(100011,i)), " ", divisor(baseConversion(100011,i)))

def gen(n, J):
	a = [''.join(i) for i in itertools.product('01', repeat=n)]
	#print(a)
	b = []
	for j in a:
		if ((j[0] == '1') and (j[n-1]=='1')):
			b.append(j)
	c = list(map(int, b))
	e = []
	m_c = 0
	for i in c:
		m = i
		d = []
		for j in range(2,11):
			d.append(baseConversion(i,j))
		#print(d)
		count = 0
		for k in range(0,9):
			if(not_prime(d[k])):
				count = count + 1;
		#print(count)
		if(count == 9):
			e.append(i)
			m_c = m_c + 1
			#print(m_c)
			if(m_c == J):
				break;
	#print(e)
	f = e[:J:]
	#print(f)
	return f

def printall(a):
	for i in a:
		d=[]
		for j in range(2,11):
			d.append(divisor(baseConversion(i,j)))
		print(i, end=' ')	
		for k in d:
			print(k, end=' ')
		print()		


x = int(input())
for i in range(0,x):
	a = input()
	b = a.split()
	c = int(b[0])
	d = int(b[1])
	print("Case #",i+1,": ", sep='')
	printall(gen(c,d))


#printall(gen(6, 3))
