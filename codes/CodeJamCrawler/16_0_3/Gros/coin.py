#!/usr/bin/python

import re, random

name='C-large.in'
f=open(name)
f_s=open(name+'_solved','w')

T=f.readline()
x=f.readline().strip().split()
N=int(x[0])
J=int(x[1])

print T,N,J

def check_div(t2):
	for x in xrange(2,101):
		if t2%x==0:
			return x
	return False

def check_all(t):
	sol=[]
	for base in range(2,11):
		t2=int(t,base)
		divisor=check_div(t2)
		if divisor!=False or divisor==t2:
			sol.append(str(divisor))
		else:
			return False
	return ' '.join(sol)

used={}
while len(used)<J:
	t='1'+''.join(['01'[random.randint(0,1)] for x in xrange(N-2)])+'1'
	if t in used:
		continue
	got=check_all(t)
	if got!=False:
		used[t]=got
		
f_s.write('Case #1:\n')
for one in used:
	f_s.write(one+' '+used[one]+'\n')

f.close()
f_s.close()