num_cases = int(raw_input())

for case in xrange(1, num_cases + 1):
	stack = raw_input()
	flips = 0
	for i in xrange(len(stack)):
		if i + 1 == len(stack):
			if stack[i] == '-':
				flips += 1
			break
		if stack[i] != stack[i+1]:
			flips += 1

	print "Case #{}: {}".format(case, flips)