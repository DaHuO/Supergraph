def get_final_num(num):
	digits = set()
	current_num = 0

	while len(digits) < 10:
		current_num += num

		new_digits = set([char for char in str(current_num)])
		digits = digits | new_digits

	return current_num

num_cases = int(raw_input())

for i in xrange(num_cases):
	starting_num = int(raw_input())
	final_num = 0

	if starting_num == 0:
		final_num = "INSOMNIA"
	else:
		final_num = get_final_num(starting_num)

	print("Case #" + str(i + 1) + ": " + str(final_num))