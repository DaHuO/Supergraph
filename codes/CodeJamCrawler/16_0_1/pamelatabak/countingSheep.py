# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
	n = int(input()) # read a list of integers, 2 in this case
	if (n == 0):
		print("Case #{}: {}".format(i, "INSOMNIA"))
		continue
	array = [0]*10
	count = 0 # counter to check if all numbers were found
	result = n
	counter = 0 # iterator, to multiply n
	while (True):
		counter+=1
		for number in str(result):
			if array[int(number) - 1] == 0:
				array[int(number) - 1] = 1
				count+=1
		if count == 10: # in case we have already found all possible numbers	
			print("Case #{}: {}".format(i, result))
			break
		else:
			result = n*counter
  # check out .format's specification for more formatting options