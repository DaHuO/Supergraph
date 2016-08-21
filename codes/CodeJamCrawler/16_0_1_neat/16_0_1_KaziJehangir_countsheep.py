# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
numTests = int(raw_input())  # read a line with a single integer
for i in xrange(1, numTests + 1):
	orignumber = int(raw_input())
	number = orignumber
	check = [0]*10
	infinitycheck = 1
	counter = 1
	while not(all(check)) and infinitycheck:
		strnumber = str(number)
		for digit in strnumber:
			check[int(digit)] = 1
			# print number
			# print check
		counter += 1
		number = orignumber * counter
		
		if counter > 1000:
			infinitycheck = 0
			print "Case #{}: {}".format(i, "INSOMNIA")
	if infinitycheck:
		print "Case #{}: {}".format(i, orignumber*(counter-1))
	# check out .format's specification for more formatting options