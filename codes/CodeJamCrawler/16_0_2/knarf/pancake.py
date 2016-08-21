import sys

def flip(stack, i):
	return map(lambda x: not x, stack[:i][::-1]) + stack[i:]

def is_happy(stack):
	for x in stack:
		if not x:
			return False
	return True

#def find_min(stack):
#	i = len(stack)-1
#	flips = 0
#	while i >= 0:
#		if not stack[i]:
#			new_stack = flip(stack,i+1)
#			if new_stack!=stack:
#				stack = flip(stack,i)
#				i-=1
#				flips+=1
#		i-=1
#		if (i<0) and (not is_happy(stack)):
#			i = len(stack)-1
#	return flips

def find_min(stack):
	i = 0
	flips = 0
	while i < (len(stack)-1):
		if (stack[i] != stack[i+1]):
			stack = flip(stack,i)
			flips+=1
		i+=1
	if not stack[i]:
		flips += 1
	return flips


n = int(sys.stdin.readline())
i = 1
for l in sys.stdin:
	stack = map(lambda x: (x == '+'), l.strip())
	print "Case #{0}: {1}".format(i,find_min(stack))
	i+=1
