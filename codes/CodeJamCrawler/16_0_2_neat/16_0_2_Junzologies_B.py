cases = input()

def flip(s):
	return "".join(map(lambda x: "+" if x == "-" else "-", s)[::-1])

for c in xrange(1,cases+1):
	stack = raw_input()
	
	flipCnt = 0
	
	# Trim the + add the end (already happy pancakes)
	stack = stack.rstrip("+")
	
	while stack != "":
		# now the end of the stack is -
		if stack[0] == "-": # Starts with -, ends with -
			iToFlip = stack.find("+") # pos of first + from Top
			if iToFlip == -1:
				iToFlip = len(stack)
		else: # Starts with +, ends with -
			iToFlip = stack.find("-") # pos of first - from Top
			if iToFlip == -1:
				iToFlip = 0
		
		stack = flip(stack[:iToFlip]) + stack[iToFlip:]
		flipCnt += 1
		stack = stack.rstrip("+")
		
	print "Case #%d: %d" % (c,flipCnt)