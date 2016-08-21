import sys

def flip(s, i):
	if (i==0):
		return s[::-1].replace('+','.').replace('-','+').replace('.','-')	
	return s[i-1::-1].replace('+','.').replace('-','+').replace('.','-')+s[i:]

[T]=[int(i) for i in sys.stdin.readline().split()]
for i in range(T):
	print ("Case #" + "{}".format(i+1) + ": ", end="")
	stack=sys.stdin.readline()[:-1]
	l=len(stack)
	count=0
	while True:
		if stack=='+'*l:
			print (count)
			break
		if stack[0]=='-':
			pos=stack.rfind('-')
			stack=flip(stack, pos+1)
		else:
			pos=stack.find('-')
			stack=flip(stack, pos)
		count=count+1
