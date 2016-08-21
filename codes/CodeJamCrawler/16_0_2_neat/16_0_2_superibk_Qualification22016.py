
def flip(to_n, pancake_stack):
	for counter, letter in enumerate(pancake_stack):
		if (letter == '-'):
			pancake_stack[counter] = '+'
		else:
			pancake_stack[counter] = '-'
		if (counter == (to_n -1) ):
			break

def get_last_unfliped(pancake_stack):
	for position, letter in enumerate(pancake_stack[::-1]):
		if (letter == '-'):
			return len(pancake_stack) - position



def run():
	input_file = open('largepancakes.in', 'r')
	output_file = open('largepancakes.out', 'w')
	first_line = input_file.readline() # read the first line of the content of the small.in file
	T = int(first_line) # convert the string file to integer
	for no in range(1, T+1):
		number = list(next(input_file))
		count = 0
		while( get_last_unfliped(number) != None):
			flip(get_last_unfliped(number), number)
			count += 1
		output_file.write('Case #{}: {}\n'.format(no, count))

run()