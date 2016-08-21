def check_min_flips(stack):
	stack = stack[::-1]
	l = len(stack)
	flips = 0

	while stack != (l * '+'):
		for num, pancake in enumerate(stack):
			if pancake == '-':
				stack = flip(stack, num)
				break
		flips += 1

	return flips


def flip(stack, num):
	new_stack = stack[0:num]
	for pancake in stack[num:]:
		if pancake == '+':
			new_stack += '-'
		else:
			new_stack += '+'

	return new_stack


def handle_input():
	i = 1
	first_line = raw_input()
	while i <= 100:
		print "Case #{}: {}".format(i, check_min_flips(str(raw_input())))
		i += 1


if __name__ == "__main__":
    handle_input()