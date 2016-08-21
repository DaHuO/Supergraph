f = open('B-large.in.txt', 'r')
T = int(f.readline())

for t in range(0,T):
	data = str(f.readline().strip())

	stack = []
	for d in data:
		if d == '+':
			stack.append(True)
		else:
			stack.append(False)

	flips = 0
	while True:

		# check to see if we are done
		done = True
		for s in stack:
			if s == False:
				done = False
				break
		if done:
			break

		# find the first index of change
		status = stack[0]
		change = len(stack)
		for i in range(1, len(stack)):
			if stack[i] != status:
				change = i
				break

		# flip all of the pancakes before the change index
		for i in range(0, len(stack)):
			if i < change:
				stack[i] = not stack[i]
		flips += 1

	print('Case #' + str(t+1) + ': ' + str(flips))
	
f.close()