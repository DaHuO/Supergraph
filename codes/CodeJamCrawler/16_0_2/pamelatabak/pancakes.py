# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer


for i in range(1, t + 1):
	result = 0
	n = raw_input() # read a sequence of pancake's state
	listPancake = list(n)
	for j in reversed(range(0, len(listPancake))):
		if listPancake[j] == "+":
			continue
		if listPancake[j] == "-":
			result+=1
			#invert the rest of the sequence
			for invert in range(0, j+1):
				if (listPancake[invert] == "+"):
					listPancake[invert] = "-"
				else:
					listPancake[invert] = "+"
	print("Case #{}: {}".format(i, result))	