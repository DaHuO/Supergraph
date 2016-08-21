#! /usr/bin/python

T=input()
A=[0]*1010
def reverse(A,n):
	for i in xrange(n/2):
		A[i],A[n-i-1]=A[n-i-1],A[i]
	for i in xrange(n):
		A[i]=not A[i]
		

def check(A,n):
	i=0
	while i<n and A[i]==1:
		A[i]=0
		i+=1
	return i

for t in xrange(T):
	s=raw_input()
	n=len(s)
	for i in xrange(n):
		if(s[i]=='+'):
			A[i]=1;
		else:
			A[i]=0
	ans=0
	while n:
		n-=1
		if A[n]==0:
			ans+=bool(check(A,n))
			ans+=1
			reverse(A,n+1)	

	print 'Case #%d:'%(t+1),ans

