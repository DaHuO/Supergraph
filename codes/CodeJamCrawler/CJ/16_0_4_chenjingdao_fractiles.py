#!/usr/bin/python

def generateSequence(K,C):
	l = 2 ** K
	arr={}
	for i in range(l):
		s = bin(i)[2:].zfill(K)
		arr[s] = s
	for j in range(C-1):
		for k in arr:
			s = ''
			for c in arr[k]:
				if c=='1':
					s += '1' * K
				else:
					s += k
			arr[k] = s

	return arr
	
def verify(g,K,C,index):
	l = K ** C
	for k in g:
		if g[k] == '0'*l:
			continue
		x=None
		for i in index:
			if x is None:
				x = g[k][i] == '0'
			else:
				x = x and g[k][i]=='0'
		if x:
			return False
	return True

def verify2(K,C,index):
	numVerified=0
	check = [False] * K
	for i in index:
		j = i
		for c in range(C):
			if not check[j%K]:
				check[j%K] = True
				numVerified += 1
			j /= K
	return numVerified == K
#K=5
#C=2
#g = generateSequence(K,C)
#for k in sorted(g.keys()):
#	print k,g[k]

#l=K ** C
#for i in range(l):
#	for j in range(i+1,l):
#		index = [i,j]
#		if not verify(g,K,C,index) == verify2(K,C,index):
#			print index

import sys
f = open('d.in')
l = int(f.readline())
for i in range(l):
	s = f.readline().split()
	K = int(s[0])
	C = int(s[1])
	S = int(s[2])
	if S < K/C:
		print 'Case #'+str(i)+": IMPOSSIBLE"
		continue
	index=[]
	n = 0
	while n < K:
		base = 1
		x = 0
		for c in range(C):
			x += n * base
			base *= K
			n += 1
			if n >= K:
				break
		index.append(x)
#	print verify2(K,C,index)
	sys.stdout.write('Case #'+str(i+1)+":")
	for x in index:
		sys.stdout.write(" "+str(x+1))
	sys.stdout.write("\n")
