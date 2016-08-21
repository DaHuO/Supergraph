# created by shikhar vishnoi

#from __future__ import print_function
import math,sys
from decimal import *
from math import *

mod=1000000007
pi=math.pi

def inp_int():
	return map(int,raw_input().split())
def inp_long():
	return map(long,raw_input().split())
def inp_float():
	return map(float,raw_input().split())
def inp_str():
	return map(str,raw_input().split())

# sys.stdin = open("input.txt",'r')
# sys.stdout = open("output.txt",'w')

#  ***********************************  #

def powl(x,y):
	num=1
	for _ in xrange(0,y):
		num = num * x
	return num

def isprime(l):
	f = long(0)
	g=min(10000000,long(math.sqrt(l))+1)
	for x in xrange(2,g):
		if (l%x) == 0:
			f = x
			break
	return f

def calc(s):
	factor = []
	s = s[::-1]
	for x in xrange(2,11):
		num=long(0)
		for y in xrange(0,len(s)):
			if s[y] == '1':
				num = num + powl(x,y)
		# print str(x) + " " + str(num)
		tmp = isprime(num)
		if tmp == 0:
			return 0
		else :
			factor.append(tmp)
	s = s[::-1]
	for x in xrange(2,11):
		s = s + ' '
		s = s + str(factor[x-2])
	print s
	return 1

def solve(n,j):
	for mask in xrange(1,(1<<(n-2))):
		s="1"
		for i in xrange(0,n-2):
			if mask & (1<<i):
				s=s+'1'
			else :
				s=s+'0'
		s=s+'1'
		if j>0:
			j = j-calc(s)
		else :
			break;

t=int(raw_input())
for x in xrange(1,t+1):
	n,j = inp_int()
	print "Case #" + str(x) + ": "
	solve(n,j)
