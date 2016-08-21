import fileinput


if __name__ == '__main__':
	lines = fileinput.input()
	next(lines)
	for case, stack in enumerate(lines):
		stack = list(reversed([c == '+' for c in stack.strip()]))
		flips = 0
		for i in xrange(len(stack)):
			if stack[i] == False:
				stack[i:] = [not p for p in stack[i:]]
				flips += 1
		print "Case #%d: %d" % (case + 1, flips)
