import sys

def read(stack):
	l = []
	for char in stack:
		if char=='+':
			l.append(1)
		elif char=='-':
			l.append(0)
	return l

def flip(l,a):
	for i in xrange(0,a):
		if l[a-i-1] == 1:
			l[i] = 0
		else:
			l[i] = 1

t = int(sys.stdin.readline())

for _ in xrange(t):
	pancakes = sys.stdin.readline()
	stack = read(pancakes)
	flipcount = 0
	top = stack[0]
	for bit in stack:
		if bit == top:
			continue
		flipcount+=1
		top = bit
	if top == 0:
		flipcount+=1
	
	print "Case #" + str(_+1) + ': ' + str(flipcount)