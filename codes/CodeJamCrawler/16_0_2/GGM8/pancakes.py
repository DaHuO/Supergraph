def flip(stack):
	stack = stack.replace("+","p")
	stack = stack.replace("-","m")
	stack = stack.replace("p","-")
	stack = stack.replace("m","+")
	return stack[::-1]

def pancakes(file):

	initial = open(file,"r")

	n = int(initial.readline())

	f = open(file,"r").readlines()

	i = 1

	for stack in (f[1:]):
		stack = stack.replace("\n","")
		sign = (stack[0] == "+")
		l = len(stack)
		count = 0

		while (stack!=("+"*l)):

			for j in xrange(l):
				# start at the top of the stack, set bool depending on what sign is
				# when prevsign != sign, flip stack(0:prev), increment count
				# if reach end and sign is false, flip stack, else return count
				# print"%s"%(stack)
				prevsign = sign
				sign = (stack[j] == "+")
				if (prevsign != sign):
					stack = flip(stack[0:j]) + stack[j:l]
					count += 1
					break

				if (not(sign) and j==(l-1)):
					stack = flip(stack)
					count += 1


		print"Case #%d: %d"%(i,count)

		i += 1








