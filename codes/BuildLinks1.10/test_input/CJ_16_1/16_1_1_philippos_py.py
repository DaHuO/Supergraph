#! /usr/bin/env python

    
import sys
f = sys.stdin.readlines()
n = int(f[0])
for i in range(1,n+1):
	s = f[i].strip()
	s2 = ""#s[0]
	
	t = []		
	for j in range(0,len(s)):
		t.append(ord(s[j])+j/100000.0)
	
	t2=list(t)
	t2.sort()
	t3 = [t2[-1]]
	index=t.index(t2[-1])
	for i2 in range(len(t2)-2,-1,-1):
		if t.index(t2[i2])<index:
			t3.append(t2[i2])
			index = t.index(t2[i2])
	for k in t3:
		s2+=chr(int(k))
	for k in t:
		if k not in t3:
			s2+=chr(int(k))
	
	print "Case #"+str(i)+": "+s2
	
