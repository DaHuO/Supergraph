def solution(starting_num):

	if starting_num == 0:
		return "INSOMNIA"

	counting_set = set()

	i = 1
	while len(counting_set) < 10:
		result = str(i * starting_num)
		counting_set.update(set(result))
		i += 1 

	return result

num_of_test_cases = int(input())

for i in range(1, num_of_test_cases + 1):

	test_case = input()
	print("Case #{}: {}".format(i, solution(int(test_case))))
