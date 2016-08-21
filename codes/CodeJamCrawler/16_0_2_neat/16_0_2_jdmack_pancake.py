def stringtobits(stack):
	new_stack = []
	for symbol in stack:
		if symbol == "+":
			new_stack.append(1)
		else:
			new_stack.append(0)
	return new_stack 

def flip(stack, tail):
	if tail == -1:
		tail = None
	else:
		tail += 1
	substack = stack[:tail]
	substack = substack[::-1]
	substack = [x ^ 1 for x in substack]
	stack[:tail] = substack

	return stack

def findstack(stack, tail=-1, flips=0):
	if 0 not in stack:
		return flips

	start = stack[0]
	end = stack[tail]

	#if start == end and start == "-":
	#	stack = flip(stack, tail)
	#	findstack(stack, tail, flips + 1)
	if start != end:
		return findstack(stack, tail - 1, flips)
	elif start == 0 and end == 0:
		stack = flip(stack, tail)
		return findstack(stack, -1, flips + 1)
	elif start == 1 and end == 1:
		if 0 not in stack[:tail]:
			stack = flip(stack, tail)
			return findstack(stack, -1, flips + 1)
		else:
			return findstack(stack, tail -1, flips)


if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		N = raw_input()
		print("Case #%i: %s" % (caseNr, findstack(stringtobits(N))))