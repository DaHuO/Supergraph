
def findFlips(string):
	stack = []

	for char in string:
		stack.append(char)

	# if len(stack) == 1:
	# 	return 0

	flips = 0
	done = 0
	doneTill = stack[0]
	while 1:
		for x in range(done, len(stack)):
			char = stack[x]
			# print char + '\t' + doneTill
			if char == doneTill:
				done = done + 1
			else:
				break

		# All chars same
		if done == len(stack):
			if '-' in stack:
				return flips + 1
			else:
				return flips

		flips = flips + 1
		for x in range(done):
			if stack[x] == '-':
				stack[x] = '+'
			else:
				stack[x] = '-'

		doneTill = stack[done-1]


t = int(raw_input())

for i in xrange(1, t + 1):
	# n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	string = str(raw_input())
	result = findFlips(string)
	print "Case #{}: {}".format(i, result)

