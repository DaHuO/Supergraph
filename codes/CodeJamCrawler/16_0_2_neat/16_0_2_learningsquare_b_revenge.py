'''def flip(stack, num_flip):
	stack_flipped = stack[num_flip-1::-1]
	for i in range(num_flip):
		stack[i] = stack_flipped[i] * -1

def count_flips(stack):
	for i in range(len(stack)):

def solve_case(stack):
	return 1'''

def solve_case(stack):
	changes = 0
	current_pancake = 1
	
	for pancake in stack[::-1]:
		if pancake != current_pancake:
			current_pancake = pancake
			changes += 1

	return changes