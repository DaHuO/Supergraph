#!/usr/bin/python
import sys 
import random 
import math 

def myint(s, b):
	tmp = s
	res = 0
	ind = 1
	while len(tmp) != 0:
		res += int(tmp[-1]) * ind
		ind *= b
		tmp = tmp[:-1]
	return res

def p(num):
	if num % 2 == 0 and num > 2: 
		return 2
	i = 3
	while True:
		if num % i == 0:
			return i
		i += 2
		#print i
		if i > 100000: #ditch it #int(math.sqrt(num)):
			break
	return 0

def myget(s):
	r = []
	for i in range(2, 11):
		#print i
		n1 = myint(s, i)
		di = p(n1)
		if di == 0:
			#prime
			return False
		r.append(di)
	return r

def r10(cur, l):
	r = '1'
	tmp = bin(cur)[2:]
	r += '0' * (l - len(tmp) - 2)
	r += tmp
	r += '1'
	return r

def g16():
	r = []
	ind = 1
	while len(r) < 1:
		n = r10(ind, 16)
		ind += 1
		if ind == 100:
			break
		g = myget(n)
		if g == False:
			continue
		print n,
		for i in g:
			print i,
		print ''
		r.append([n, g])
	return r

def g32():
	r = []
	ind = 1
	while len(r) < 500:
		n = r10(ind, 32)
		ind += 1
		#if ind % 100 == 0:
		#print ind
		g = myget(n)
		if g == False:
			continue
		print n,
		for i in g:
			print i,
		print ''
		r.append([n, g])
	return r

print 'Case #1:'
if len(sys.argv[1]) > 1:
	g32()
else:
	g16()
