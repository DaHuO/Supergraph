import sys
import re

'''
This solution is based on the understanding that consequentive chars
count as a single of their sign. I basically want to merge groups together,
but we can only merge one at a time. Therefore we will count the number of merges
to perform, plus if we need a finishing opposite sign flip. For example, given
+++---+--+, we can see it's equivilent to +-+-+.
The steps to win are:
1. Flip the first three,  ------+--+ (-+-+)
2. Flip the first six,    +++++++--+ (+-+)
3. Flip the first seven,  ---------+ (-+)
4. Flip the first eight,  ++++++++++ (+)
'''

def parse(lines):
	'''Parse the stack file'''
	next(lines) # Get rid of first line

	for line in lines:
		line = line.replace('\n','')
		yield line

def simplify(stack):
	'''Simplify a stack to it's simple form as explained above'''
	stack = re.sub(r'\++', '+', stack)
	stack = re.sub(r'-+', '-', stack)
	return stack

def solve(stack):
	'''Find the minimal number of flips to perform to solve a stack'''
	stack = simplify(stack)
	merges = len(stack) - 1 # Number of merges to perform
	last_flip = 1 if stack[-1]=='-' else 0 # Check whether after merges another flip is needed
	return merges + last_flip

def main():
	# Expect to receive the input file name
	if len(sys.argv) < 2:
		print('Missing input file argument')
		sys.exit(1)

	input_file = sys.argv[1]
	with open(input_file) as ifile:
		for i, stack in enumerate(parse(ifile)):
			min_flips = solve(stack)
			result_line = 'Case #{i}: {flips}'.format(i=i+1, flips=min_flips)
			print(result_line)

if __name__=='__main__':
	main()
