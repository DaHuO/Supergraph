# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 23:09:21 2016

@author: dan
"""
import math
def isprime(x):
	
	for i in range(2,int(math.sqrt(x))):
		if x%i==0:
			return i
	return -1

def ispass(x):
	div=[]
	num=bin(x)[2:]
	div.append(num)
	for i in range(2,11):
		tem=isprime(int(num,i))
		if tem==-1:
			return False
		else:
			div.append(tem)
	for j in div:
		print j,
	print ""
	return True		
		
	
def solve(m,n):
	#m is length, n is number
	index=0
	length=int(m)
	number=int(n)
	starter=int(math.pow(2,length-1)+3)
	endd=int(math.pow(2,length))	
	for i in range(starter,endd,2):
		if index==number:
			break
		else:
			if ispass(i):
				index=index+1	 


	


t = int(raw_input())  # read a line with a single integer

m,n=(raw_input().strip()).split(' ')
print "Case #1: "
solve(m,n)
