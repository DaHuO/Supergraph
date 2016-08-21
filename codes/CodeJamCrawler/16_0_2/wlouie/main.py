def dp(L, memo):
	min_flips = float("inf")
	if L in memo and memo[L] >= 0:
		return memo[L]
	elif count(L, '-') == len(L):
		memo[L] = 1
		return 1
	elif count(L, '+') == len(L):
		memo[L] = 0
		return 0
	else:
		for i in xrange(len(L)):
			flipped_L = flip(L,i)
			if flipped_L in memo:
				if memo[flipped_L] == -1:
					continue
			else:
				memo[flipped_L] = -1
			num_flips = 1 + dp(flip(L,i), memo)

			if num_flips < min_flips:
				min_flips = num_flips
				memo[L] = min_flips
	return min_flips

def bfs_soln(goal):
	visited = set()
	all_good = tuple(['+' for j in xrange(len(goal))])
	queue = [(all_good, 0)]
	if goal == all_good:
		return 0
	while queue:
		seq, num_flip = queue.pop(0)
		for i in xrange(len(seq)):
			flipped_seq = flip(seq, i)
			if flipped_seq == goal:
				return num_flip + 1
			if flipped_seq not in visited:
				visited.add(flipped_seq)
				queue.append((flipped_seq, num_flip + 1))
	return None




def flip(L, i):
	newL = list(L)
	for j in xrange(i + 1):
		newL[j] = negate(L[i - j])
	return tuple(newL)

def count(L, char):
	total = 0
	for c in L:
		if c == char:
			total += 1
	return total

def negate(char):
	if char == '-':
		return '+'
	return '-'

def revenge_of_pancakes(L):
	return dp(tuple(L), {})



if __name__ == "__main__":
	# input_file = "A-large.in"
	input_file = "B-small-attempt0.in"
	output_file = "part_B_output.txt"
	with open(input_file, 'rb') as f:
		with open(output_file, 'wb') as o:
			T = f.readline()
			for i, line in enumerate(f):
				answer = bfs_soln(tuple(line.rstrip()))
				o.write("Case #" + str(i + 1) + ": " + str(answer) + "\n")
	# for i in xrange(4):
	# 	print flip('----', i)
	# print dp(tuple('+++'), {})
	# for thing in ['-', '-+', '+-', '+++', '--+-']:
	# # print revenge_of_pancakes('--+---+---')
	# 	print bfs_soln(tuple(thing))

	# print count('--+-', '+')