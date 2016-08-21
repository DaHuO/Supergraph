#revenge_of_the_pancakes.py
def test(stack):

	x = 0

	while stack[-1:] == '+': stack = stack[:-1]

	while len(stack) > 0:

		if stack[0] == '-':
			if stack.find('+') < 0: return x+1
			stack = stack[stack.find('+'):]
			x += 1
		else:
			if stack.find('-') < 0: return x+1
			stack = stack[stack.find('-'):]
			x += 1

	return x

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
 	n = raw_input()
 	print "Case #{}: {}".format(i, test(n))
