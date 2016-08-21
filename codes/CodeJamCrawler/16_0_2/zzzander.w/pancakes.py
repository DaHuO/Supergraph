def flipStack(stack):
	stack = stack.replace('-', '1')
	stack = stack.replace('+', '-')
	stack = stack.replace('1', '+')
	return stack

input = file('B-large.in', 'r')
T = int(input.readline().strip())
for X in range(1,T+1):
	stack = list(input.readline().strip())
	pancakes = ''.join(map(str, stack))
	flips = 0
	for y in range(len(pancakes)):
		z = len(pancakes) - 1
		if pancakes[z:] == '-':
			flips += 1
			pancakes = flipStack(pancakes)
		pancakes = pancakes[:z]
	print "Case #%d:" % X,flips
