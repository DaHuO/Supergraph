def solve(filename):
	with open(filename, 'r') as f:
		number_of_test_cases = int(f.readline())

		for i in range(number_of_test_cases):
			last_number_seen = count_numbers(int(f.readline()))
			print("Case #{}: {}".format(i + 1, last_number_seen)) 


def count_numbers(n):
	non_updating_turns = 0
	current_number = n
	i = 2

	numbers_seen = set(str(current_number))

	while len(numbers_seen) != 10:
		current_number = i * n
		digits = set(str(current_number))

		last_set_size = len(numbers_seen)
		numbers_seen |= digits
		if len(numbers_seen) == last_set_size:
			non_updating_turns += 1
		else:
			non_updating_turns = 0

		if non_updating_turns == 100:
			return 'INSOMNIA' 
		
		i += 1

	return current_number

# solve('small_input.txt')
solve('large_input.txt')
