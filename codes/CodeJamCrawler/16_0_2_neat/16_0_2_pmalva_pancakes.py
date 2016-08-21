T = int(raw_input())

def flip(stack,i):
	beg = stack[:i+1]
	stack = beg[::-1] + stack[i+1:]
	for j in xrange(i+1):
		if stack[j] == '+':
			stack = stack[:j]+'-'+stack[j+1:]
		else:
			stack = stack[:j]+'+'+stack[j+1:]
	return stack

def obtainMinSwap(stack,steps):
	while len(stack)>0 and stack[-1]=='+':
		stack = stack[:-1]

	last = '+'
	if len(stack)>0 and stack[0] == '+':
		last = '-'
	for i in stack:
		if i != last:
			steps+=1
		last = i
	return steps
	

for i in xrange(1,T+1):
	stack = raw_input()
	print "Case #"+str(i)+": "+str(obtainMinSwap(stack,0))
