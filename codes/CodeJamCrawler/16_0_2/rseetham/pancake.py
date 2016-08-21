def pancake (stack) :
	stack = list(stack)
	l = len(stack)
	count = 0
	for i in range(l-1,-1,-1) :
		if stack[i] == '-' :
			stack = change(stack, i)
			count = count + 1
	return str(count)

def change(stack, i) :
	for j in range (0, i + 1) :
		if stack[j] == '-' :
			stack[j] = '+'
		elif stack[j] == '+' :
			stack[j] = '-'
	return stack

if __name__ == '__main__':
	try :
		t = int(input())
		for i in range(1, t + 1):
			s = input()
			print("Case #%i: %s" % (i, pancake(s)))
	except EOFError:
		print ("Error: EOF or empty input!")