#! /usr/bin/env python
import sys
f = sys.stdin.readlines()
n = int(f[0])
for i in range(1,n+1):
	x=int(f[i])
	a = set()
	if x==0:
		print "Case #"+str(i)+": "+"INSOMNIA"
		continue
	N=0
	#k=0
	while len(a)!=10:		
		N+=1
		k=N*x
		#print "===="
		while k!=0:
			#print k
			a.add(k%10)			
			k=k/10
	print "Case #"+str(i)+": "+str(N*x)	
