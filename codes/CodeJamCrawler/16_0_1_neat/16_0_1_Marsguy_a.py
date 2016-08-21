
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for T in xrange(1, t + 1):
	n = int(raw_input())

	if n == 0:
		print "Case #{}: INSOMNIA".format(T)
	else:
		digits = [0] * 10
		lastn = n
		stop = False
		i = 1
		while stop == False:
			lastn = n * i
			lastndigits = list(str(lastn))
			for x in lastndigits:
				digits[int(x)] = 1 

			if min(digits) > 0:
				stop = True
			i = i+1


		# read a list of integers, 2 in this case
		print "Case #{}: {}".format(T, lastn)
		# check out .format's specification for more formatting options