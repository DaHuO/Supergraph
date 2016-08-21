
# def pancakes(stack):
# 	# Returns the minimum number of flips to get a happy stack
# 	# of pancakes.

# 	starting_stack = stack
# 	frontier = []
# 	starting_cost = 0
# 	heappush(frontier, (starting_cost, starting_stack))
# 	explored = set()
# 	goal = '+'*len(stack)

# 	while frontier:
# 		print 'Exploring new frontier'
# 		(stack_cost, stack_state) = heappop(frontier)


# 		# If the stack is fully happy, no flips are required.
# 		if stack_state == goal:
# 			return stack_cost

# 		# add the stack state to the set of explored states
# 		explored.add(stack_state)

# 		# Identify neighbouring states
# 		# print 'Current stack: ', stack_state
# 		for i in xrange(len(stack_state)):

# 			substack = stack_state[:i+1]
# 			flipped_substack = flip(substack)
# 			neighbour_state = flip(stack_state[:i+1]) + stack_state[i+1:]

# 			# print 'Flipping index ', i
# 			# print 'Substack: ', substack
# 			# print 'Flipped Substack: ', flipped_substack
# 			# print 'Neighbour State: ', neighbour_state

# 			# This whole thing sucks because I didn't set up the data structures for the nodes properly.
# 			if neighbour_state not in explored:

# 				# Check if the neighbour state exists in the frontier
# 				if neighbour_state not in [fs for (fc, fs) in frontier]:
# 					heappush(frontier, (stack_cost+1, neighbour_state))

# 				else:
# 					# Search the frontier states for the neighbouring state
# 					for (i, (c,v)) in enumerate(frontier):

# 						# If there is an entry with the same state and greater cost,
# 						# replace it with the neighbour and rebalance the heap.
# 						if neighbour_state == v and stack_cost+1 < c:
# 							frontier[i] = (stack_cost+1, neighbour_state)
# 							print 'Heapifying'
# 							heapify(frontier)
# 							break

# def flip(stack):
# 	# Flips a stack of pancakes.
# 	# The order of pancakes is reversed,
# 	# and the sign of each individual pancake is also reversed.

# 	flipped = []
# 	for s in reversed(stack):
# 		if s == '+':
# 			flipped.append('-')
# 		elif s == '-':
# 			flipped.append('+')

# 	return ''.join(flipped)

def pancakes(starting_stack):

	stack = simplify(starting_stack)

	# if the bottom pancake is bad, need to do at least one flip.
	if stack[-1] == '-':
		final_flip = 1
	else:
		final_flip = 0

	# Otherwise, flip one less times than the number of cakes (+1 if necessary for the final flip).
	num_flips = len(stack) - 1 + final_flip
	return num_flips

def simplify(stack):
	# Simplifies a stack of pancakes by merging runs of consecutive
	# pancakes to a single patty.

	simplified = []
	first_cake = True
	for s in stack:
		# to avoid out of index errors.
		if first_cake:
			simplified.append(s)
			first_cake = False
			continue

		if s != simplified[-1]:
			simplified.append(s)

	return ''.join(simplified)



if __name__ == '__main__':

	num_test_cases = int(raw_input())

	for i in xrange(1, num_test_cases+1):
		stack = raw_input() #[p for p in raw_input()]
		result = pancakes(stack)

		print 'Case #{}: {}'.format(i, result)