
def problem_b(pancakes):
	flip_count = 0
	while not flips_complete(pancakes):
		side = pancakes[0]
		size = 1
		for i in range(1, len(pancakes)):
			if pancakes[i] != side:
				size = i
				break
		else:
			size = len(pancakes)
		pancakes = flip_pancakes(pancakes, size)
		flip_count += 1
	return flip_count

def flip_pancakes(pancakes, n):
	flipped_pancakes = list(reversed(pancakes[:n])) + pancakes[n:]
	for i in range(n):
		flipped_pancakes[i] = not flipped_pancakes[i]
	return flipped_pancakes

def flips_complete(pancakes):
	return sum(pancakes) == len(pancakes)

def pancakes_from_str(s):
	pancakes = []
	for c in s:
		if c == '\n':
			break
		pancakes.append(c == '+')
	return pancakes

def read_input(filename):
	with open('output.txt', 'w') as output_file:
		with open(filename) as input_file:
			T = int(input_file.readline())
			for i in range(T):
				s = input_file.readline()
				output_file.write('Case #{:d}: {:d}\n'.format(i + 1, problem_b(pancakes_from_str(s))))

read_input('B-large.in')