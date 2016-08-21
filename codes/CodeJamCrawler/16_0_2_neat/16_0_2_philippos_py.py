#! /usr/bin/env python
import sys
f = sys.stdin.readlines()
n = int(f[0])
for i in range(1,n+1):
	s = f[i].strip()
	a = [s[j]=='+' for j in range(len(s))]
	#print a
	N=0
	last=a[0]
	regions=1
	for j in range(1,len(s)):
		if a[j]!=last:
			regions+=1
		last = a[j]
	N=regions-1
	if last==False:
		N+=1
	print "Case #"+str(i)+": "+str(N)	
