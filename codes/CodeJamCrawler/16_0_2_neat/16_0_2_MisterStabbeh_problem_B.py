def solution(stack_of_pancakes):
	num_of_flips = 0
	last_pancake = None

	for pancake in stack_of_pancakes:
		if last_pancake == None:
			last_pancake = pancake

		if pancake != last_pancake:
			num_of_flips += 1
			last_pancake = pancake

	if last_pancake == '-':
		num_of_flips += 1

	return num_of_flips

num_of_test_cases = int(input())

for i in range(1, num_of_test_cases + 1):

	test_case = input()
	print("Case #{}: {}".format(i, solution(test_case)))
