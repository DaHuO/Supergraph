import sys

def main():
	num_test_cases = int(sys.stdin.readline())
	for i in range(num_test_cases):
		input = str(sys.stdin.readline())
		print("Case #%d: %d" % (i + 1, flip_pancake(list(input[:len(input)]))))

def flip_pancake(stack):
	if '\n' in stack:
		stack.remove('\n')
	if (stack == '-'):
		return 1
	flips = 0
	while (True):
		flip_range = 0
		if (stack[0] == '+'):
			while (stack[flip_range] == '+'):
				flip_range += 1
				if flip_range >= len(stack):
					return flips
			stack = flip(stack, 0, flip_range)
			flips += 1
		flip_range = len(stack)
		while (stack[flip_range - 1] == '+'):
			flip_range -= 1
			if flip_range <= 0:
				return flips
		stack = flip(stack, 0, flip_range)
		flips += 1
	return -1

def flip(pancakes, start, end):
	temp = pancakes[start:end]
	temp = temp[::-1]
	pancakes = temp + pancakes[end:]
	for i in range(start,end):
		if (pancakes[i] == '+'):
			pancakes[i] = '-'
		else:
			pancakes[i] = '+'
	return pancakes
if __name__ == "__main__":
    main()
