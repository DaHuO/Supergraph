#! /usr/bin/env python
import sys
import math
f = sys.stdin.readlines()
n0 = int(f[0])

R=1
for i in range(1,n0+1):
	f[i] = f[i].strip().split()
	f[i][0],f[i][1]=f[i][0],int(f[i][1])
	if int(f[i][0])>R:
		R=f[i][0]
		R=int(R)
	#print "Case #"+str(i)+": "+str(N)	

R=10**R-1
#a = [True] * (R+1)                       
#a[0] = a[1] = False
#for (i, prime) in enumerate(a):
#	if prime:		
#		for n in xrange(i*i, R, i):  
#			a[n] = False
def a(g):
	#result=True
	if g%2==0:# or g%5==5:
		return False
	for m in range(3,int(math.sqrt(g)),2):
		#if m%5==0:
		#	m+=2
		if g%m==0:
			return False
	return True

def nontrivialDivisor(g):
	if g%2==0:
		return 2
	#if g%5==0:
	#	return 5	
	m=3
	while True:
		#if m%5==0:
		#	m+=2	
		if g%m==0:# a[m] and
			#print g
			return m
		m+=2
			
for i in range(1,n0+1):
	print "Case #"+str(i)+":"
	#print i
	count = 0
	res=[]
	for x in range(2**(int(f[i][0])-1),2**(int(f[i][0]))):
		#print x
		#continue
		if a(x):
			continue
		prime = False 
		x1=	(bin(x)[2:])
		if x1[-1]=='0':
			continue
		for base in range(2,10+1):
			#x = f[i][0]
			sum=0
			bini=x
			for c in range(int(f[i][0])):
				sum+=(base**c)*(bini&1)
				bini=bini>>1
			#print sum
			#exit
			if a(sum):# or sum%2==0:
				prime = True
				#print ((x1,sum,base))
				break
		if not prime:
			#print "ok"
			count+=1
			e=[]
			for base in range(2,10+1):				
				sum=0
				#print i
				for c in range(int(f[i][0])):
					sum+=(base**c)*int(x1[len(x1)-c-1])
				e.append(nontrivialDivisor(sum))
			res.append(e)
			print x1+" "+str(e).replace("[","").replace("]","").replace(",","").replace("(","").replace(")","")
			if count==int(f[i][1]):
				break
		
				
				
