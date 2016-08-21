#! /usr/bin/python

def getdigit(n,a):
	while n:
		a[n%10]+=1
		n/=10

def solve(n):
	a=[0]*10	
	t=1
	while(1):
		getdigit(n*t,a)
		sign=1
		for i in a:
			if(not i):sign=0;break;
		if(sign):
			break;
		if(t>100):
			return 0
		t+=1	
	return t;	
		

T=input()
for t in xrange(T):
	n=input()
	ans=solve(n)
	print 'Case #%d:'%(t+1),
	if(ans):
		print ans*n
	else:
		print 'INSOMNIA' 

''' gen data
import random
n=30
print n
for i in xrange(n):
	print random.randint(1,1000000)
'''	
		

