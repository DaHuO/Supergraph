#!/usr/bin/python
import sys
import time
def main(size):
	"""
	@param size = string; small or large
	"""
	infile = size + "_b.in"

	output = ""

	with open(infile) as file:
		num_cases = int(file.readline())
		for case in range(1, num_cases+1):
			num_flips = compute_num_flips(file.readline())
			output += "Case #%s: %s\n" % (case, num_flips)
	with open(size + "_b.out", 'w') as outfile:
		outfile.write(output)


def compute_num_flips(stack):
	"""
	@param stack = string of "+" and "-"
	"""
	stack = list(stack.strip())
	height = len(stack)
	# Naive strategy : try flipping the bottom-most not flipped each time	
	stack.reverse() # now the start of the list is the bottom of the stack
	num_flips = 0

	while True:
		try:
			last_blank = stack.index("-")
		except ValueError: # if all are happy already
			return num_flips

		# top must be "-" before you flip so it will be "+" when flipped
		if stack[-1] != "-":
			first_blank = height - stack[::-1].index("-") - 1
			# flip everything after the first blank pancake
			flip(stack, first_blank + 1)
			num_flips += 1
		flip(stack, last_blank)
		num_flips += 1
	
	
def flip(stack, index):
	"""
	@param stack = list; will be reversed from i: and the signs changed
	"""
	swap_map = {"+": "-", "-": "+"}
	stack[index:] = reversed([swap_map[elem] for elem in stack[index:]])	

			
if __name__ == "__main__":
	main(sys.argv[1])

