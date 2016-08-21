# Code Jam 2016: Problem 2

def make_happy_pancakes(stack):
	last = len(stack) - 1
	flips = 0

	while sum(stack) < len(stack):
		for i in range(last, -1, -1):
			if not stack[i]:
				last = i
				break
		
		first = -1

		for i in range(len(stack)):
			if not stack[i]:
				first = i - 1
				break

		if first >= 0:
			stack = flip_pancakes(stack, first)
			flips += 1

		stack = flip_pancakes(stack, last)
		flips += 1

	return flips

def flip_pancakes(stack, index):
	for i in range(index + 1):
		if not stack[i]:
			stack[i] = 1
		else:
			stack[i] = 0
	return stack

# Read line with the number of cases
t = int(input())
for i in range(1,t+1):
	stack = [1 if s == '+' else 0 for s in input()]
	res = make_happy_pancakes(stack)
	print("Case #{}: {}".format(i, res))