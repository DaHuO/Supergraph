#
#	Arshan Alam
#
#	Google Code Jam 2016
#
#	Revenge of the Pancakes
#

for test in range(1, int(input())+1):
	stack = list()
	num_flips = 0
	for c in str(input()):
		if c is "+":
			stack.append(1)
		else:
			stack.append(0)
	stack_len = len(stack)
	while sum(stack) != stack_len:
		start_bit = stack[0]
		for i, b in enumerate(stack):
			if b == start_bit:
				stack[i] = 1-start_bit
			else:
				break
		num_flips += 1

	print("Case #" + str(test) + ": " + str(num_flips))
