
def turn(pancake):
	if pancake == '-':
		return '+'
	else:
		return '-'

def flip(pancakes, start, end):
	while start < end:
		pancakes[start] = turn(pancakes[start])
		pancakes[end] = turn(pancakes[end])
		pancakes[start], pancakes[end] = pancakes[end], pancakes[start]
		start += 1
		end -= 1
	if start == end:
		pancakes[start] = turn(pancakes[start])

def count_moves(pancakes):
	last_index = len(pancakes) - 1
	n_moves = 0
	while last_index >= 0:
		if pancakes[last_index] == '-':
			if pancakes[0] == '+':
				index = 1
				while pancakes[index] == '+' and index < last_index:
					index += 1
				flip(pancakes, 0, index - 1)
				n_moves += 1
			flip(pancakes, 0, last_index)
			n_moves += 1
		last_index -= 1
	return n_moves

T = int(raw_input())
test = 0
while test < T:
	n_moves = 0
	pancakes = list(raw_input())
	n_moves = count_moves(pancakes)
	test += 1
	print "Case #%d: %d" % (test, n_moves)