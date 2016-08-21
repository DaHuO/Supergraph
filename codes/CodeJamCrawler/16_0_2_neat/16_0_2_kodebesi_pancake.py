import sys

def reduceStack(stack):
	result = ''
	while True:
		if len(stack) < 2:
			result = result + stack
			if len(result) > 1:
				if result[-1] == result[-2]:
					return result[0:-1]
			return result
		if len(result) == 0 or result[-1] != stack[0]:
			result += (stack[0])
		if stack[0] == stack[1]:		
			stack = stack[2:]
		else:
			stack = stack[1:]

inputFile = sys.argv[1]
f = open(inputFile, 'r')
content = f.readlines()
T = int(content[0])
for t in range(0,T):
	stack = reduceStack(content[t+1].strip())
	if stack[-1] == '+':
		v = 0
	else:
		v = 1
	print 'Case #' + str(t+1) + ': ' + str(len(stack) - 1 + v)
f.close()