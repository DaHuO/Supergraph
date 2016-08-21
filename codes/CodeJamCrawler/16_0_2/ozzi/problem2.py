def pancake_stack(pancakes):
	"""
	Function that takes in a stack of pancakes and outputs the
	minimum number of moves required to get them happy side up '+'

	:param pancakes: current stack of pancakes 
	:return n: number of minimum flips needed
	"""
	
	n = 0

	pancakes = pancakes[::-1]

	for i in xrange(len(pancakes)):
		if pancakes[i] is '+':
			continue
		else:
			n += 1
			pancakes  = pancakes[0:i] + flip(pancakes[i:])

	return n


def flip(pancakes):
	"""
	Helper function to flip a pancake stack

	:param pancakes: stack of pancakes
	:return pancakes: stack of pancakes after flip
	"""

	for i, pancake in enumerate(pancakes):
		if pancake is '+':
			pancakes[i] = '-'
		else:
			pancakes[i] = '+'

	return pancakes


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
m = []
for i in xrange(1, t + 1):
  m .append(raw_input())  # read a list of integers, 2 in this case

for i, pancakes in enumerate(m):
	print ("Case #" + str(i+1) + ": " + str(pancake_stack([pancake for pancake in pancakes]))) 

# sample = ['-', '-', '+', '-']
# print (flip(sample))
# print (pancake_stack(sample))