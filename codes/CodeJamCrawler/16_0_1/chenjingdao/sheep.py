#!/usr/bin/python

def getLastNumber(n):
	numZeros=0
	for i in range(len(n)):
		if not n[len(n)-1-i]=='0':
			break
		numZeros += 1
	if numZeros > 0:
		m = n[:-numZeros]
	else:
		m = n
	if len(m)==0:
		return 'INSOMNIA'
	seen = [False] * 10
	offset = ord('0')
	if numZeros > 0:
		seen[0] = True
		numSeen = 1
	else:
		numSeen = 0
	x = int(m)
	y = x
	iters = 0
	while True:
		iters += 1
		s = str(y)
#		z = 0
#		for i in range(len(s)):
#			if not s[len(s)-1-i]=='0':
#				break
#			z += 1
#		if z > 0:
#			s = s[:-z]
#			numZeros += z
#			if not seen[0]:
#				numSeen += 1
#			x = int(s)
#			y = x
		for c in s:
			if not seen[ord(c)-offset]:
				seen[ord(c)-offset] = True
				numSeen += 1
		if numSeen >= 10:
			break
		y += x
	s = str(y)
	for i in range(numZeros):
		s += '0'
#	global maxIters
#	if iters > maxIters:
#		maxIters = iters
#		print n,x,iters
	return s

#maxIters=0
#for i in range(1000001):
#	getLastNumber(str(i))
f = open('a.in')
l = int(f.readline())
for i in range(l):
	n = f.readline().strip()
	print 'Case #'+str(i+1)+": "+getLastNumber(n)
