SIDE_UP = "+"
SIDE_DOWN = "-"
import sys


def print_output(answer,index):
	print "Case #{0}: {1}".format(index,answer)

def inverse(pancake_stack):
	inversed_stack = ""
	for x in pancake_stack:
		if x == SIDE_UP:
			inversed_stack += SIDE_DOWN
		else:
			inversed_stack += SIDE_UP
	return inversed_stack


def flip_pancake(index,pancake_stack,cache):
	if (index,pancake_stack) in cache:
		# print >> sys.stderr , "cache hit"
		return cache[(index,pancake_stack)]

	flipped = pancake_stack[0:index+1]
	rest = pancake_stack[index+1:]
	flipped = flipped[::-1]
	flipped = inverse(flipped)
	result = flipped+rest
	cache[(index,pancake_stack)] = result
	return result

def found(pancake_stack,target):
	return pancake_stack == target

def find_best_flip(pancake_stack):
	best_index = []

	for index,p in enumerate(pancake_stack):
		if index == 0:
			prev = p
		else:
			if p != prev:
				best_index.append(index-1)

			prev = p
	if len(best_index) == 0:
		best_index = [len(pancake_stack)-1]
	return best_index

def find_shortest_flip(pancake_stack,cache):

	target = ""
	for _ in range(len(pancake_stack)):
		target += SIDE_UP

	queue = [(0,pancake_stack)]
	
	visited = []
	target_found = False
	while not target_found:
		distance,curr = queue.pop(0)
		# print queue,visited,curr,target,"curr target"
		visited.append(curr) 
		target_found = found(curr,target)

		if target_found:
			break
		else:
			l_high_target_flip = find_best_flip(curr)
			for i in l_high_target_flip:

				next = flip_pancake(i,curr,cache)
				# print i,next,"next"


				if next in visited:
					continue
				else:
					queue.append((distance+1,next))


	return distance

len_input = int(raw_input())
cache = {}
for case_num in range(len_input):
	_input = raw_input()
	print >> sys.stderr , "case {0}".format(case_num)
	flip = find_shortest_flip(_input,cache)

	print_output(flip,case_num+1)
