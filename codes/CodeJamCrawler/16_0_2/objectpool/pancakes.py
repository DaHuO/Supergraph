

def flip_bits(bits):
	return [ 1 if b == 0 else 0 for b in bits ]

def get_potential_transformations(leaf):
	results = set()

	leaf_length = len(leaf)
	if leaf_length == 1:
		results.add(tuple(flip_bits(leaf)))
		return results

	flip_type = leaf[0]
	num_bits_to_flip_at_start = None
	# print leaf, leaf[0]
	for b in range(1, leaf_length):
		if leaf[b] != flip_type:
			# print leaf[b]
			num_bits_to_flip_at_start = b
			break
			# print 'yay', num_bits_to_flip_at_start
	# print '\t', num_bits_to_flip_at_start, leaf[:num_bits_to_flip_at_start], leaf[num_bits_to_flip_at_start:]
	flipped_bits = flip_bits(leaf[:num_bits_to_flip_at_start])
	if len(flipped_bits) == leaf_length:
		transformation = flipped_bits
	else:
		transformation = flipped_bits + leaf[num_bits_to_flip_at_start:]
	results.add(tuple(transformation))
	return results

def solution(inpt):
	bit_tuple = tuple([ 1 if c == "+" else 0 for c in inpt ])
	goal_tuple = tuple([1]*len(inpt))
	num_flips = 0
	num_zeroes = bit_tuple.count(0)
	num_ones = bit_tuple.count(1)
	# if num_zeroes > num_ones:

	if bit_tuple != goal_tuple:

		leaves = []
		leaves.append(bit_tuple)

		visited = set()
		while leaves:
			num_flips += 1
			leaf = leaves.pop()
			visited.add(leaf)
			new_leaves = get_potential_transformations(list(leaf))
			# print leaf, new_leaves
			win = False
			for new_leaf in new_leaves:
				if new_leaf == goal_tuple:
					win = True
					break
				elif new_leaf not in visited:
					leaves.append(new_leaf)
			if win:
				return num_flips
	else:
		return 0
	return num_flips

t = int(input())

for test_index in range(t):
	test_case = input()
	soln = solution(test_case)
	print('Case #'+str(test_index+1)+': ' + str(soln))


