# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

# takes in (current number, accumulator, base number). If number is seen,
# mark as true in accumulator. Returns current number when elts of A are true
def count_sheep_recursive(n, A, base):
	#base case: check if all elements in A are true
	check = True
	for i in range (10):
		if not(A[i]):
			check = False
			break
	if check: return n

	#recursive case: go through all the digit, set to true
	n = n + base
	n1 = n
	while (n1 != 0):
		last_digit = n1%10
		A[last_digit] = True
		n1 = n1/10

	return count_sheep_recursive(n, A, base)


# Counting Sheep: if all digits 0 to 9 are seen, then return last seen number
# return INSOMNIA otherwise.
def counting_sheep(n):
	# if divisible by 5, always count forever
	if (n == 0):
		return "INSOMNIA"
	# else keep going and check 
	else:
		A = [] # accumulate truthness of all numbers
		for i in range (10): #0 to 9
			A.append(False)
		return count_sheep_recursive(0, A, n)
	
#taken from https://code.google.com/codejam/tutorials.html
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, counting_sheep(n[0]))
  # check out .format's specification for more formatting options